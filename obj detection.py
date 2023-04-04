import cv2
import numpy as np
import pyttsx3
import keyboard
from easyocr import Reader
import argparse
import speech_recognition as sr
import wikipedia
import datetime
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon !")  
  
    else:
        speak("Good Evening !") 

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

wishMe()

while True:
        
    query = takeCommand().lower()
        
    # All the commands said by user will be
    # stored here in 'query' and will be
    # converted to lower case for easily
    # recognition of command
    if  'search' in query:
        speak('Searching ...')
        query = query.replace("search", "")
        results = wikipedia.summary(query, sentences = 3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif  'camera' in query :
        confThreshold = 0.5

        nmsThreshold = 0.3

        whT = 320

        classesFile = 'coco.names'
        classNames = []
        with open(classesFile, 'rt') as f:
            classNames = f.read().rstrip('\n').split('\n')
        # print(classNames)
        # print(len(classNames))

        modelConfiguration = 'yolov3-320.cfg' 
        modelWeights = 'yolov3-320.weights'
        net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        def findObjects(outputs,img):
            hT, wT, cT = img.shape
            bbox = []
            classIds = []
            confs = []

            for output in outputs:
                for det in output:
                    scores = det[5:]
                    classId = np.argmax(scores)
                    confidence = scores[classId]
                    if confidence > confThreshold:
                        w,h = int(det[2]*wT),int(det[3]*hT)
                        x,y = int((det[0]*wT)-w/2), int((det[1]*hT)-h/2)
                        bbox.append([x,y,w,h])
                        classIds.append(classId)
                        confs.append(float(confidence))
            #print(len(bbox))
            indicies = cv2.dnn.NMSBoxes(bbox,confs,confThreshold,nmsThreshold)
            j = indicies[:]
            speak("There are  ")
            for i in range(len(j)):
                # i = i[0]
                box = bbox[j[i]]
                x,y,w,h = box[0],box[1],box[2],box[3]
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
                cv2. putText (img, f'{classNames[classIds[j[i]]].upper()} {int(confs[j[i]]*100)}%',(x+10,y+20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)
                
                speak(classNames[classIds[j[i]]])
                if i == len(j)-1:
                    engine.runAndWait() 
                else :  
                    speak("and ")
                     


        img = cv2.imread("dog.jpg")
        x = np.array(img).shape

        blob = cv2.dnn.blobFromImage(img,1/255,(whT,whT),[0,0,0],1,crop=False)
        net.setInput(blob)

        layerNames = net.getLayerNames()
        #print(layerNames)
        outputNames = [layerNames[i-1] for i in net.getUnconnectedOutLayers()]
        # print(outputNames)

        outputs = net.forward(outputNames)

        # print(outputs[0][0])

        findObjects(outputs,img)

        while (x[0] >= 1080 or x[1] >= 1920):
            img = cv2.resize(img,(int(x[1]/2),int(x[0]/2)),interpolation= cv2.INTER_AREA)
            x = np.array(img).shape
        cv2.imshow('Image',img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif  'video' in query :

        cap = cv2.VideoCapture(0)

        confThreshold = 0.5

        nmsThreshold = 0.3

        whT = 320

        classesFile = 'coco.names'
        classNames = []
        with open(classesFile, 'rt') as f:
            classNames = f.read().rstrip('\n').split('\n')
        # print(classNames)
        # print(len(classNames))

        modelConfiguration = 'yolov3-320.cfg' 
        modelWeights = 'yolov3-320.weights'
        net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

        def findObjects(outputs,img):
            hT, wT, cT = img.shape
            bbox = []
            classIds = []
            confs = []

            for output in outputs:
                for det in output:
                    scores = det[5:]
                    classId = np.argmax(scores)
                    confidence = scores[classId]
                    if confidence > confThreshold:
                        w,h = int(det[2]*wT),int(det[3]*hT)
                        x,y = int((det[0]*wT)-w/2), int((det[1]*hT)-h/2)
                        bbox.append([x,y,w,h])
                        classIds.append(classId)
                        confs.append(float(confidence))
                        
            indicies = cv2.dnn.NMSBoxes(bbox,confs,confThreshold,nmsThreshold)
            for i in indicies:
                box = bbox[i]
                x,y,w,h = box[0],box[1],box[2],box[3]
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
                cv2. putText (img, f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)
                speak(classNames[classIds[i]])
                

                        
        while True:
            success,img = cap.read()
            
            blob = cv2.dnn.blobFromImage(img,1/255,(whT,whT),[0,0,0],1,crop=False)
            net.setInput(blob)

            layerNames = net.getLayerNames()

            outputNames = [layerNames[i-1] for i in net.getUnconnectedOutLayers()]

            outputs = net.forward(outputNames)
            


            findObjects(outputs,img)

            cv2.imshow('Image',img)

            cv2.waitKey(3000)
            takeCommand()
            if 'close' in query :
                speak ("camera closed")
                break
            

        cap.release()
        cv2.destroyAllWindows()

    elif 'read' in query : 


        from easyocr import Reader
        import argparse
        import cv2
        import pyttsx3
        engine = pyttsx3.init()

        def cleanup_text(text):
            # strip out non-ASCII text so we can draw the text on the image
            return "".join([c if ord(c) < 128 else "" for c in text]).strip()


        args = ["C://Users//20109//Documents//projects//Ro2ya//images//oc.png","en",-1]

        # break the input languages into a comma separated list
        langs = args[1].split(",")
        print("[INFO] OCR'ing with the following languages: {}".format(langs))
        # load the input image from disk
        image = cv2.imread(args[0])
        # OCR the input image using EasyOCR
        print("[INFO] OCR'ing input image...")
        reader = Reader(langs, gpu=args[2] > 0)
        results = reader.readtext(image,paragraph="True")


        # loop over the results
        for (bbox, text)  in results:
            # display the OCR'd text and associated probability
            print("[INFO] : " , text)
            # unpack the bounding box
            (tl, tr, br, bl) = bbox
            tl = (int(tl[0]), int(tl[1]))
            tr = (int(tr[0]), int(tr[1]))
            br = (int(br[0]), int(br[1]))
            bl = (int(bl[0]), int(bl[1]))
            # cleanup the text and draw the box surrounding the text along
            # with the OCR'd text itself
            text = cleanup_text(text)
            engine.say(text)
            engine.runAndWait() 
            cv2.rectangle(image, tl, br, (0, 255, 0), 2)
            cv2.putText(image, text, (tl[0], tl[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        # show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(0)

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("% H:% M")   
        speak(f"the time now is {strTime}")
    elif 'mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")


# import the necessary packages
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
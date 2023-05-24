.![Picture1](https://user-images.githubusercontent.com/99560022/229833089-aa339dc1-de9f-4d14-80e7-d3d3632db092.png)

# ROAYA: Assisting the Blind with AI

ROAYA is a software program designed to empower blind individuals by enabling them to navigate and interact with the world independently. Leveraging various AI techniques such as computer vision and natural language processing (NLP), ROAYA aims to provide a comprehensive solution for blind users to learn about the surrounding environment. This project incorporates object detection and optical character recognition (OCR) functionalities to enhance the user experience.

## Features

1. **Voice Interaction**: The program utilizes speech recognition and text-to-speech synthesis to allow users to interact with ROAYA through voice commands and receive audio responses.

2. **Wikipedia Search**: Users can ask ROAYA to search for information on various topics using natural language commands. The program utilizes Wikipedia's API to retrieve summarized results and speaks them out to the user.

3. **Object Detection**: ROAYA integrates computer vision techniques to detect objects in images captured by a camera. It employs the YOLO (You Only Look Once) algorithm with pre-trained weights to identify objects and provides an audio description of the detected objects.

4. **Real-Time Object Detection**: In addition to image-based object detection, ROAYA can perform real-time object detection using a webcam. It continuously analyzes the video feed, detects objects, and provides audio descriptions of the identified objects.

5. **Optical Character Recognition (OCR)**: ROAYA incorporates OCR functionality to extract text from images. It uses the EasyOCR library to recognize text in images, and the extracted text is converted to speech and read aloud to the user.

6. **Current Time**: The program can provide the current time to the user upon request.

7. **Email Sending**: ROAYA offers the ability to send emails. Users can dictate the content of the email, specify the recipient, and the program will send the email using a configured SMTP server.

## Requirements

To run ROAYA, the following dependencies are required:

- Python 3.7 or above
- OpenCV (cv2)
- Numpy
- Pyttsx3
- Keyboard
- EasyOCR
- SpeechRecognition
- Wikipedia
- Datetime
- Smtplib

The required versions of each package may vary, so it's recommended to create a virtual environment and install the dependencies listed in the `requirements.txt` file.

## Usage

1. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

2. Run the `ROAYA.py` file:
   ```
   python ROAYA.py
   ```

3. Ensure that your microphone and camera (if using real-time object detection or OCR) are properly connected and configured.

4. Follow the voice prompts and provide voice commands to interact with ROAYA. Examples of commands include:
   - "Search for <topic>"
   - "Open camera"
   - "Start video"
   - "Read image"

5. ROAYA will process the commands, perform the requested tasks, and provide audio responses or visual outputs accordingly.

## Limitations

- The accuracy of object detection and OCR depends on the quality of the input images and the environmental conditions (e.g., lighting, image clarity).
- The current implementation only supports English language recognition for speech and text analysis.
- The program may encounter difficulties recognizing certain accents or pronunciations during speech recognition.

## Disclaimer

ROAYA is an ongoing project aimed at assisting blind individuals. However, it may not encompass all possible scenarios or address every individual's needs. This software should be used as a supplementary tool and should not replace the assistance of human guides or professionals.
  

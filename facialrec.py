import cv2
import os
import speech_recognition as sr
import numpy as np
from picamera import PiCamera
from time import sleep

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to get a speech response
def get_speech(prompt):
    with sr.Microphone() as source:
        print(prompt)
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            response = recognizer.recognize_google(audio)
            print("You said: " + response)
            return response
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return None

def capture_face(image_path='captured_face.jpg'):
    camera = PiCamera()
    camera.start_preview()
    sleep(2)  # Allow the camera to warm up
    camera.capture(image_path)
    camera.stop_preview()
    camera.close()
    print(f"Face captured and saved as {image_path}")

def main():
    # Capture the face and save the image
    face_image_path = 'captured_face.jpg'
    capture_face(face_image_path)

    # Load the captured image
    img = cv2.imread(face_image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        print("No face detected. Please try again.")
        return

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Save the image with detected face
    detected_face_image_path = 'detected_face.jpg'
    cv2.imwrite(detected_face_image_path, img)
    print(f"Face detection completed and saved as {detected_face_image_path}")

    # Questions to ask
    questions = [
        "What is your ethnic background?",
        "What cultural practices do you engage in?",
        "Do you engage in multiple cultural practices?",
        "Would you consider your identity to be multicultural?"
    ]

    responses = {}

    # Ask each question and store the response
    for question in questions:
        response = None
        while response is None:
            response = get_speech(question)
        responses[question] = response

    print("\nSummary of Responses:")
    for question, response in responses.items():
        print(f"{question}: {response}")

if __name__ == "__main__":
    main()

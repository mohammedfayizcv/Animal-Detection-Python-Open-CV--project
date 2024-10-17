import cv2
import tkinter as tk
from tkinter import messagebox
import numpy as np
import pygame  # Import pygame for sound
import serial  # Import serial library for Arduino communication

# Initialize pygame mixer
pygame.mixer.init()

# Load the siren sound
siren_sound = pygame.mixer.Sound("siren.wav")  # Ensure you have this file in the same directory

# Load YOLO
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]  
layer_names = net.getLayerNames()
output_layers = [layer_names[net.getUnconnectedOutLayers()[0] - 1]]

# Initialize serial communication with Arduino
# ser = serial.Serial('COM22', 9600, timeout=1)  # Replace 'COM3' with your Arduino's serial port

def detect_animals():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()
        if not ret:
            print("Error: Unable to read from camera")
            break

        height, width, channels = img.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        animal_detected = False
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                if label in ["dog", "cat", "bird", "horse", "cow", "sheep", "elephant", "bear", "zebra", "giraffe"]:
                    animal_detected = True
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, label, (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

        cv2.imshow('Image', img)
        if cv2.waitKey(1) == ord('q'):
            break

        if animal_detected:
            messagebox.showinfo("Animal Detection", "Animal detected!")
            siren_sound.play()  # Play the siren sound
            print("Animal Detection")
            ser.write(b'Animal Confirmed\n')  # Send confirmation to Arduino
            break

    cap.release()
    cv2.destroyAllWindows()

root = tk.Tk()
root.title("Animal Detection System")
root.geometry("800x600")  # Set the window size to 800x600

title_label = tk.Label(root, text="Animal Detection System", font=("Arial", 24))
title_label.pack(pady=20)

button = tk.Button(root, text="Start Detection", command=detect_animals, font=("Arial", 18), bg="green", fg="white")
button.pack(pady=20)

root.mainloop()
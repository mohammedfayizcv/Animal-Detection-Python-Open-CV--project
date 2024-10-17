# Animal-Detection-Python-Open-CV

Project Overview
This project involves creating an Animal Detection System that uses computer vision to identify animals in real-time through a webcam. If an animal is detected, the system triggers an alarm and communicates with an Arduino to send alerts, which may include sending SMS notifications with GPS coordinates.

Components Used

Hardware:
Webcam: For capturing video input.
Arduino Board: This is used to process input from sensors and control output devices.
Ultrasonic Sensors: These are used to measure distance and detect nearby objects.
Laser Module and LDR (Light Dependent Resistor): This is for tripwire functionality to detect interruptions.
Buzzer: To sound an alarm when an animal is detected.
GPS Module: To get the location of the event.
GSM Module: To send SMS alerts.

Software:
OpenCV: For real-time computer vision tasks.
Tkinter: For creating a graphical user interface (GUI) in Python.
Pygame: For playing sound effects.
Serial Communication: To communicate between Python and Arduino.
Functionality

Animal Detection:
The Python script uses YOLO (You Only Look Once), a real-time object detection system, to identify animals in the webcam feed.
Detected animals are highlighted with bounding boxes, and if specific animals (e.g., dog, cat, etc.) are detected, an alert is triggered.
Alarm System:

When an animal is detected, a siren sound is played, and an alert message box is displayed.
The system sends a confirmation message to the Arduino via serial communication.

Arduino Response:
The Arduino monitors ultrasonic sensors and the LDR to check for nearby objects or interruptions.
When an animal is confirmed by the Python script, the Arduino activates the buzzer and sends an SMS with the GPS location.

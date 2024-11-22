# Animal-Detection-Python-Open-CV

## Project Overview
This project involves creating an **Animal Detection System** that uses computer vision to identify animals in real-time through a webcam. When an animal is detected, the system triggers an alarm and communicates with an Arduino to send alerts, including SMS notifications with GPS coordinates.

---

## Components Used

### Hardware:
- **Webcam**: Captures video input for animal detection.
- **Arduino Board**: Processes input from sensors and controls output devices.
- **Ultrasonic Sensors**: Measures distance and detects nearby objects.
- **Laser Module and LDR (Light Dependent Resistor)**: Implements tripwire functionality to detect interruptions.
- **Buzzer**: Sounds an alarm when an animal is detected.
- **GPS Module**: Provides the location of the detection event.
- **GSM Module**: Sends SMS alerts to notify stakeholders.

### Software:
- **OpenCV**: Handles real-time computer vision tasks.
- **Tkinter**: Creates a graphical user interface (GUI) in Python.
- **Pygame**: Plays sound effects for the alarm system.
- **Serial Communication**: Enables communication between Python and Arduino.

---

## Functionality

### Animal Detection:
- The Python script uses **YOLO (You Only Look Once)**, a real-time object detection system, to identify animals in the webcam feed.
- Detected animals are highlighted with bounding boxes.
- If specific animals (e.g., dogs, cats) are detected, an alert is triggered.

### Alarm System:
- When an animal is detected:
  - A siren sound is played using **Pygame**.
  - An alert message box is displayed via **Tkinter**.
  - A confirmation message is sent to the Arduino via serial communication.

### Arduino Response:
- The Arduino continuously monitors:
  - **Ultrasonic sensors** for nearby objects.
  - **LDR (Light Dependent Resistor)** for interruptions in the laser beam (tripwire functionality).
- Upon confirmation from the Python script, the Arduino:
  - Activates the **buzzer** to sound an alarm.
  - Sends an SMS alert with the GPS location via the **GSM module**.

---

## How to Run the Project
1. **Hardware Setup**:
   - Connect the webcam, Arduino, ultrasonic sensors, LDR, buzzer, GPS module, and GSM module according to the project schematic.
2. **Software Setup**:
   - Install the required Python libraries:
     ```bash
     pip install opencv-python pygame
     ```
   - Ensure the Arduino code is uploaded, and serial communication is properly configured.
3. **Run the Python Script**:
   - Start the detection system:
     ```bash
     python animal_detection.py
     ```
   - The GUI will launch, displaying the webcam feed and real-time detections.

---

## Future Enhancements
- Improve animal classification accuracy with fine-tuned YOLO weights.
- Add a feature to record and store detection events in a database.
- Integrate cloud-based notification systems for more robust alerts.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
- [YOLO Object Detection](https://pjreddie.com/darknet/yolo/)
- OpenCV and Python communities for their extensive documentation and support.

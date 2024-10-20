# Iot-Based-Forest-Fire-Monitoring-System

**Description:** This project is designed to monitor forest fires in real-time using two sensors (temperature and flame detection). The system is powered by an ESP32 microcontroller, which reads data from the sensors and uploads it to a real-time database. The data is then displayed on a web application developed using HTML, CSS, and JavaScript.

## Project Overview:

**Microcontroller:** ESP32 is used for reading sensor values and sending the data to a real-time Firebase database.

**Sensors:**

**Temperature & Humidity Sensor (DHT11):** Monitors the environmental temperature and humidity.

**Flame & Smoke Sensors:** Detects the presence of fire and smoke in the vicinity.

**Real-Time Database:** The system uses Firebase for storing and retrieving sensor data in real-time.

**Web Application:** A web app is developed to visualize the data collected from the sensors and monitor the forest conditions remotely.

**Hardware Requirements:**

ESP32 Microcontroller

DHT11 Temperature & Humidity Sensor

Flame Sensor

Smoke Sensor

Buzzer (for alerts)

## Software Requirements:

**Arduino IDE:** For programming the ESP32 microcontroller.

**Python:** For serial communication and uploading data to Firebase.

**Firebase:** Used as the real-time database to store sensor readings.

**HTML, CSS, and JavaScript:** For developing the web application.

## Setup and Usage:

## Arduino Setup:

Connect the sensors (DHT11, flame, and smoke sensors) to the ESP32 microcontroller as per the connections in the Forest_Fire.ino file.

Flash the Forest_Fire.ino code to the ESP32 using Arduino IDE.

## Python Script:

The Python script reads data from the ESP32 via serial communication and uploads it to Firebase.

Ensure the serial port is correctly set and connected.

Run the script to continuously monitor and upload data to Firebase.

## Web Application:

The web app fetches data from Firebase and displays it in a user-friendly interface.

Refer to the HTML, CSS, and JavaScript files for setting up the web interface and configuring the database connection.

## Features:

**Real-Time Monitoring:** Monitors temperature, humidity, flame, and smoke levels in real-time.

**Alerts:** Activates a buzzer when the system detects smoke or flames.
**Web Interface:** Displays sensor data on the web app for remote monitoring.
**Future Enhancements:**

Integration of additional sensors for more comprehensive monitoring.

Deployment of a mobile app for real-time notifications and alerts.

Implementation of AI-based algorithms for early forest fire prediction.

For detailed code and setup instructions, refer to the Python script and Arduino code files. The web application code (HTML, CSS, and JavaScript) is also provided for building the web interface and connecting it to the database.

**Disclaimer:** This project is for demonstration and educational purposes only. It should not be used as a standalone solution for critical real-world applications without further validation and testing.


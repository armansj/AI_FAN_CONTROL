#Ultrasonic Radar System with Servo Motor and Buzzer

This project is an ultrasonic radar system that uses a servo motor, an ultrasonic sensor, and a buzzer to detect nearby objects and alert the user when objects are within a certain range. The radar scans an area by rotating the servo motor and measuring the distance to objects using the ultrasonic sensor. If an object is detected within 10 cm, the buzzer will beep.

Hardware Components

Microcontroller (e.g., ESP32, Raspberry Pi Pico)
Servo Motor (for rotating the radar sensor)
Ultrasonic Sensor (for measuring the distance to objects)
Buzzer (for alerting when objects are too close)
Jumper wires
Breadboard
Pin Configuration:
Pin 0: Servo motor control
Pin 1: Ultrasonic sensor trigger
Pin 2: Ultrasonic sensor echo
Pin 3: Buzzer control
Features

Servo-based scanning: The servo motor rotates the ultrasonic sensor from 0 to 180 degrees.
Distance measurement: Uses an ultrasonic sensor to detect the distance to objects.
Buzzer alert: When an object is closer than 10 cm, the buzzer will beep.
Asynchronous control: The radar system runs asynchronously using the uasyncio library, allowing smooth, continuous operation.
Software Dependencies

This code is written in MicroPython and uses the following libraries:

machine: For controlling GPIO pins and the PWM signal for the servo motor.
time: For handling timing operations.
uasyncio: For asynchronous tasks that run in the background without blocking other operations.
How It Works

Servo Motor: The servo motor moves the ultrasonic sensor to scan an area. It rotates between 0° and 180°, making small steps (5° in this case) with each iteration.
Ultrasonic Sensor: The ultrasonic sensor sends a pulse and measures the time it takes for the pulse to reflect back after hitting an object. This time is converted into a distance value.
Buzzer: If the distance to an object is less than 10 cm, the buzzer is triggered to alert the user. Otherwise, the buzzer remains off.
Asynchronous Scanning: The radar continuously scans using asynchronous code, ensuring smooth operation and allowing other tasks (like reading the sensor or moving the servo) to happen simultaneously.

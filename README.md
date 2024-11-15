Overview

This project uses a Raspberry Pi Pico to measure the distance to an object using an HC-SR04 Ultrasonic Distance Sensor. Depending on the detected distance, an RGB LED will light up with different colors to visually indicate the proximity of the object.

Key Features:

The green LED lights up for distances greater than 30 cm.
The yellow LED lights up for distances between 10 cm and 30 cm.
The red LED lights up for distances less than or equal to 10 cm.
No resistors are used in the circuit because we’re confident the Raspberry Pi Pico's GPIO pins can handle the LEDs directly without overloading.

Components Required

Raspberry Pi Pico (RP2040 microcontroller)
HC-SR04 Ultrasonic Distance Sensor
RGB LED (common cathode or common anode)
Jumper wires
Breadboard (optional)
Pinout Configuration

HC-SR04 Ultrasonic Sensor:

VCC → 5V (Pin 36 on Raspberry Pi Pico)
GND → GND (Pin 38 on Raspberry Pi Pico)
Trig → GP1 (Pin 2 on Raspberry Pi Pico)
Echo → GP0 (Pin 1 on Raspberry Pi Pico)

RGB LED:

Red → GP4 (Pin 5 on Raspberry Pi Pico)
Yellow → GP3 (Pin 4 on Raspberry Pi Pico)
Green → GP2 (Pin 3 on Raspberry Pi Pico)
GND (common cathode) → GND (Pin 38 on Raspberry Pi Pico)
Note: No resistors are included in the circuit, as we rely on the Raspberry Pi Pico's ability to handle the current directly.

Software Setup

Requirements:

MicroPython installed on your Raspberry Pi Pico.
Thonny or any other MicroPython-compatible IDE.
Steps to Get Started:
Install MicroPython on your Raspberry Pi Pico:
Follow the official guide to get MicroPython installed on your Raspberry Pi Pico.

Upload the Code:

You can use the Python code in the repository to control the ultrasonic sensor and RGB LED based on the detected distance.

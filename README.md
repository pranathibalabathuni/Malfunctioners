# Malfunctioners
# LiDAR Sensor System using Arduino & Python

## Overview

This project implements a low-cost 2D LiDAR sensor system using an Arduino-based microcontroller. The system measures distances using a VL53L0X Time-of-Flight (ToF) sensor mounted on a stepper motor. The collected data is transmitted via serial communication to a Python script, which processes and visualizes the mapped environment in real time.

## Features

- **Distance Measurement**: Uses the VL53L0X ToF sensor to measure distances.
- **Rotational Scanning**: The sensor is mounted on a 28BYJ-48 stepper motor, controlled via ULN2003 driver.
- **Real-Time Data Transmission**: Sends data via serial communication to a Python script.
- **Graphical Visualization**: The scanned environment is plotted using Python's Matplotlib.
- **Integration with Arduino IDE & VS Code**: Development and testing in Arduino IDE and VS Code.

## Components

- **Microcontroller**: ESP32 DevKit
- **Distance Sensor**: VL53L0X
- **Stepper Motor**: 28BYJ-48
- **Motor Driver**: ULN2003A
- **Software Tools**:
  - Arduino IDE (for microcontroller programming)
  - Python (for data visualization) {Mapping the real time using pyserial}
  - VS Code (for development)

## Installation & Setup

### 1. Hardware Connections

- Connect VL53L0X sensor to ESP32 (I2C communication - SDA/SCL pins)
- Connect 28BYJ-48 stepper motor to ULN2003 driver, and then to ESP32 (GPIO pins)

### 2. Software Installation

#### Arduino Code

1. Install the Arduino IDE and required ESP32 board libraries.
2. Install the VL53L0X library (`Adafruit_VL53L0X`).
3. Upload the Arduino sketch to ESP32.

#### Python Visualization

1. Install Python 3.x and required libraries:
   ```bash
   pip install pyserial matplotlib
   ```
2. Run the Python script to receive serial data and plot the map:
   ```bash
   python lidar_plot.py
   ```

## Usage

1. Power the ESP32 and run the Arduino code.
2. Ensure the stepper motor is rotating and scanning.
3. Start the Python script to visualize the scanned area.

## Future Improvements

- Implement ROS2 integration for enhanced mapping.
- Improve real-time plotting performance.
- Add obstacle detection and alerting features.

##

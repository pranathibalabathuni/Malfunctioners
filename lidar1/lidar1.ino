#include <Arduino.h>
#include <Wire.h>
#include <AccelStepper.h>
#include <Adafruit_VL53L0X.h>

// Stepper Motor Pins (Adjust according to wiring)
#define MOTOR_PIN1 26
#define MOTOR_PIN2 25
#define MOTOR_PIN3 33
#define MOTOR_PIN4 32

#define STEPS_PER_REV 2048  // Steps per full revolution

// Create Stepper object
AccelStepper stepper(AccelStepper::FULL4WIRE, MOTOR_PIN1, MOTOR_PIN3, MOTOR_PIN2, MOTOR_PIN4);

// Create ToF Sensor object
Adafruit_VL53L0X tof_sensor = Adafruit_VL53L0X();

void setup() {
    Serial.begin(115200);
    while (!Serial) { delay(1); }
    Serial.println("ESP32 LiDAR System Starting...");

    Wire.begin();
    if (!tof_sensor.begin()) {
        Serial.println(F("Failed to boot VL53L0X"));
        while (1);
    }
    Serial.println(F("VL53L0X Sensor Detected!"));

    stepper.setMaxSpeed(3000);
    stepper.setAcceleration(1000);
}

void scanAndMeasure(int direction) {
    for (int angle = 0; angle < 360; angle += 2) {
        stepper.move(direction * (STEPS_PER_REV / 360) * 2);
        stepper.runToPosition();
        
        VL53L0X_RangingMeasurementData_t measure;
        tof_sensor.rangingTest(&measure, false);

        Serial.print(angle);
        Serial.print(",");
        if (measure.RangeStatus != 4) {
            Serial.println(measure.RangeMilliMeter);
        } else {
            Serial.println("Out of range");
        }
        delay(50);
    }
}

void loop() {
    scanAndMeasure(1);  // Clockwise rotation
    scanAndMeasure(-1); // Counterclockwise rotation
    Serial.println("Completed one full CW and CCW rotation.");
    while (1); // Halt further execution
}

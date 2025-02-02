import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

# Set up Serial connection (change COM port if needed)
try:
    ser = serial.Serial('COM7', 115200, timeout=1)
    print("Connected to serial port.")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit(1)

# Initialize data storage
x_vals = []
y_vals = []

# Initialize plot
fig, ax = plt.subplots()
scatter = ax.scatter(x_vals, y_vals, s=10, c='blue')  # Scatter plot for points

# Set up plot labels and grid
ax.set_xlabel("X (cm)")
ax.set_ylabel("Y (cm)")
ax.set_title("Real-Time Object Mapping")
ax.grid(True)

# Set fixed plot limits for -50 cm to 50 cm
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)

# Variables to track last data received time
last_data_time = time.time()
timeout = 2  # Timeout in seconds

def update(frame):
    global x_vals, y_vals, last_data_time

    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(f"Received: {line}")  # Debug: Print raw data
            last_data_time = time.time()
            # Skip lines that don't contain a comma
            if "," not in line:
                return scatter,

            # Parse angle and distance
            try:
                angle, distance = map(int, line.split(','))
            except ValueError:
                print(f"Skipping invalid data: {line}")
                return scatter,

            # Convert to radians
            theta = np.radians(angle)

            # Convert to Cartesian (assuming distance in mm)
            x = (distance * np.cos(theta)) / 10  # Scale to cm
            y = (distance * np.sin(theta)) / 10  # Scale to cm

            # Append new coordinates to the lists
            x_vals.append(x)
            y_vals.append(y)

            # Keep last 200 points for better mapping
            if len(x_vals) > 200:
                x_vals.pop(0)
                y_vals.pop(0)

            # Update scatter plot data
            scatter.set_offsets(np.column_stack((x_vals, y_vals)))

            # Print angle and distance in cm
            print(f"Angle: {angle}°, Distance: {distance / 10:.2f} cm, X: {x:.2f} cm, Y: {y:.2f} cm")
        else:
            # Check if timeout has occurred
            if time.time() - last_data_time > timeout:
                print("No data received for {} seconds. Assuming rotations are done.".format(timeout))
                plt.savefig("pic.png")  # Save the plot as an image file
                print("Plot saved as pic.png")
                plt.close(fig)  # Close the plot
                ser.close()  # Close the serial connection
                exit(0)  # Exit the program
    except Exception as e:
        print(f"Error: {e}")

    return scatter,

# Setup live plotting
ani = animation.FuncAnimation(fig, update, interval=100, blit=True, cache_frame_data=False)

# Show the plot
plt.show()

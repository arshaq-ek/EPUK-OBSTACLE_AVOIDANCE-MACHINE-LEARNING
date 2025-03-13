"""epuk_obstacle-avoidance controller."""

# Import necessary modules from the Webots controller.
from controller import Robot, Motor, DistanceSensor, Keyboard
import csv

# Create the Robot instance.
robot = Robot()

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# Define the wheels and initialize them.
wheels = []
wheelnames = ['left wheel motor', 'right wheel motor']
for name in range(2):
    wheels.append(robot.getDevice(wheelnames[name]))
    wheels[name].setPosition(float('inf'))
    wheels[name].setVelocity(0.0)

# Define the distance sensors and enable them.
ds = []
ds_names = ['ps7', 'ps0', 'ps6', 'ps1']
for x in range(len(ds_names)):
    ds.append(robot.getDevice(ds_names[x]))
    ds[x].enable(timestep)

# Initialize the keyboard.
keyboard = Keyboard()
keyboard.enable(timestep)

# Define maximum speed.
maxspeed = 3

# Open a CSV file to store the data.
with open("robot_data.csv", "w", newline="") as csvfile:
    # Create a CSV writer object.
    csvwriter = csv.writer(csvfile)

    # Write the header row.
    csvwriter.writerow(["LeftSpeed", "RightSpeed", "FrontRight", "FrontLeft", "SideLeft", "SideRight"])

    # Main simulation loop.
    while robot.step(timestep) != -1:
        # Initialize wheel speeds to 0.
        left_speed = 0.0
        right_speed = 0.0

        # Retrieve wheel instances.
        leftwheel = wheels[0]
        rightwheel = wheels[1]

        # Read distance sensor values.
        front_left = ds[0].getValue()
        front_right = ds[1].getValue()
        side_left = ds[2].getValue()
        side_right = ds[3].getValue()

        # Get keyboard input.
        key = keyboard.getKey()

        # Adjust speeds based on key presses.
        if key == 317:  # Down arrow
            left_speed = -maxspeed
            right_speed = -maxspeed
        elif key == 315:  # Up arrow
            left_speed = maxspeed
            right_speed = maxspeed
        elif key == 314:  # Left arrow
            left_speed = -maxspeed / 5
            right_speed = maxspeed
        elif key == 316:  # Right arrow
            left_speed = maxspeed
            right_speed = -maxspeed / 5

        # Set wheel velocities.
        leftwheel.setVelocity(left_speed)
        rightwheel.setVelocity(right_speed)

        # Write data to the CSV file.
        csvwriter.writerow([left_speed, right_speed, front_right, front_left, side_left, side_right])
        csvfile.flush()  # Ensure data is written immediately.

        # Print data to the console.
        print(f"Left Speed: {left_speed:.2f}, Right Speed: {right_speed:.2f}, "
              f"Front Right: {front_right:.2f}, Front Left: {front_left:.2f}, "
              f"Side Left: {side_left:.2f}, Side Right: {side_right:.2f}")

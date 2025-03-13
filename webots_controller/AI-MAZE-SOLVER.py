from controller import Robot, DistanceSensor, Motor
import joblib

# Load the trained model and scaler
model = joblib.load(r"C:\Users\arsha\OneDrive\Documents\epukl\controllers\wall_follower-epuk\robot_speed_predictor.pkl")
scaler = joblib.load(r"C:\Users\arsha\OneDrive\Documents\epukl\controllers\wall_follower-epuk\scaler.pkl")

# Initialize the robot and its components
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Initialize the wheels
wheels = []
wheelnames = ['left wheel motor', 'right wheel motor']
for name in range(2):
    wheels.append(robot.getDevice(wheelnames[name]))
    wheels[name].setPosition(float('inf'))  # Set to infinite position for velocity control
    wheels[name].setVelocity(0.0)  # Start with zero velocity

# Initialize the distance sensors
ds = []
ds_names = ['ps7', 'ps0', 'ps6', 'ps1']  # Names of the distance sensors
for sensor_name in ds_names:
    sensor = robot.getDevice(sensor_name)
    sensor.enable(timestep)
    ds.append(sensor)

# Main control loop
while robot.step(timestep) != -1:
    # Read sensor values
    front_left = ds[0].getValue()
    front_right = ds[1].getValue()
    side_left = ds[2].getValue()
    side_right = ds[3].getValue()

    # Prepare sensor values as input for the model
    sensor_values = [[front_right, front_left, side_left, side_right]]
    scaled_values = scaler.transform(sensor_values)  # Scale the sensor values

    # Predict wheel speeds using the model
    predicted_speeds = model.predict(scaled_values)
    left_speed, right_speed = predicted_speeds[0]  # Extract predicted speeds

    # Set the wheel velocities
    wheels[0].setVelocity(left_speed)  # Left wheel
    wheels[1].setVelocity(right_speed)  # Right wheel

    # Print the sensor values and wheel speeds for debugging
    print(f"FrontRight: {front_right:.2f}, FrontLeft: {front_left:.2f}, SideLeft: {side_left:.2f}, SideRight: {side_right:.2f}")
    print(f"Predicted Left Speed: {left_speed:.2f}, Predicted Right Speed: {right_speed:.2f}")

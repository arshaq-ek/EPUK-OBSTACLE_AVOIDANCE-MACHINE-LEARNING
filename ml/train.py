import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Step 1: Load the Dataset
data = pd.read_csv(r"C:\Users\arsha\OneDrive\Documents\epukl\controllers\wall_follower-epuk\robot_data.csv")

# Step 2: Prepare Features and Target Variables
X = data[["FrontRight", "FrontLeft", "SideLeft", "SideRight"]]  # Features (sensor readings)
y = data[["LeftSpeed", "RightSpeed"]]  # Target (wheel speeds)

# Step 3: Split the Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Scale the Features
scaler = StandardScaler()  # Normalize sensor values to improve model performance
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 5: Train the Machine Learning Model
model = RandomForestRegressor(random_state=42, n_estimators=100)
model.fit(X_train_scaled, y_train)

# Step 6: Evaluate the Model
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")

# Step 7: Save the Model and Scaler
joblib.dump(model, r"C:\Users\arsha\OneDrive\Documents\epukl\controllers\wall_follower-epuk\robot_speed_predictor.pkl")
joblib.dump(scaler, r"C:\Users\arsha\OneDrive\Documents\epukl\controllers\wall_follower-epuk\scaler.pkl")
print("Model and Scaler saved successfully!")

# Step 8: Predict Speeds for New Sensor Values
new_sensor_values = [[105.23, 98.45, 110.12, 67.89]]  # Replace with actual sensor readings
new_sensor_values_scaled = scaler.transform(new_sensor_values)  # Scale the new data

predicted_speeds = model.predict(new_sensor_values_scaled)
print(f"Predicted Left Speed: {predicted_speeds[0][0]:.2f}, Predicted Right Speed: {predicted_speeds[0][1]:.2f}")

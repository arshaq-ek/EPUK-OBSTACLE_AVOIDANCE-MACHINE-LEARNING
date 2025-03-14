# EPUK Obstacle Avoidance Using Machine Learning

## 🚀 Overview
This project focuses on obstacle avoidance for autonomous robots using **machine learning techniques**. The system takes sensor data, processes it, and predicts the best path to avoid obstacles efficiently.

## 🛠 Features
- **Machine Learning-Based Navigation**: Uses a trained model to predict obstacle-free paths.
- **Data Preprocessing**: Standardization and scaling of sensor data.
- **Random Forest Regression**: Implements a machine learning model for decision-making.
- **Performance Evaluation**: Uses MSE (Mean Squared Error) to measure model accuracy.

## 📂 Project Structure
```
EPUK-OBSTACLE_AVOIDANCE-MACHINE-LEARNING/
│-- data/                   # Training dataset
│-- models/                 # Saved machine learning models
│-- scripts/                # Training and evaluation scripts
│-- main.py                 # Entry point for obstacle avoidance
│-- requirements.txt        # Required dependencies
│-- README.md               # Project documentation
```

## 📦 Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/arshaq-ek/EPUK-OBSTACLE_AVOIDANCE-MACHINE-LEARNING.git
cd EPUK-OBSTACLE_AVOIDANCE-MACHINE-LEARNING
pip install -r requirements.txt
```

## 🔧 Usage
Run the main script to start the obstacle avoidance system:
```bash
python main.py
```

## 🧠 Machine Learning Model
- **Algorithm**: Random Forest Regressor
- **Libraries Used**:
  - `pandas` for data handling
  - `scikit-learn` for ML modeling
  - `joblib` for model saving/loading

## 🏆 Performance Evaluation
The model is evaluated using **Mean Squared Error (MSE)** to ensure high accuracy in predicting obstacle-free paths.

## 🛠 Dependencies
The project requires the following Python packages:
```txt
pandas
scikit-learn
joblib
```
To install them, run:
```bash
pip install -r requirements.txt
```

## 🤝 Contributing
Feel free to fork this repository, create a branch, and submit a pull request! 🎯

## 📜 License
This project is licensed under the MIT License.

---
### 🔗 Repository Link
[GitHub Repo](https://github.com/arshaq-ek/EPUK-OBSTACLE_AVOIDANCE-MACHINE-LEARNING)


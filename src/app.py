from flask import Flask, request, jsonify
import pandas as pd
from src.data_loader import load_data
from src.model import preprocess_data, train_model
from src.monitor import monitor_sensor_data, diagnose_fault
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

app = Flask(__name__)

# List of sensor files
sensor_files = [
    'PS1.txt', 'PS2.txt', 'PS3.txt', 'PS4.txt', 'PS5.txt', 'PS6.txt',
    'EPS1.txt', 'FS1.txt', 'FS2.txt', 'TS1.txt', 'TS2.txt', 'TS3.txt',
    'TS4.txt', 'VS1.txt', 'CE.txt', 'CP.txt', 'SE.txt'
]

# Load and preprocess data
data = load_data(sensor_files, 'profile.txt')
X = data.iloc[:, :-5]
y = data.iloc[:, -5:].idxmax(axis=1)  # Assuming the last 5 columns are the target labels

# Preprocess data
X_normalized, scaler = preprocess_data(data)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)

# Train the model
model = train_model(X_train, y_train)

# Print classification report
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

@app.route('/monitor', methods=['POST'])
def monitor():
    incoming_data = request.json
    new_data = pd.DataFrame(incoming_data)
    prediction = monitor_sensor_data(model, scaler, new_data)
    diagnosis = diagnose_fault(prediction)
    return jsonify({'prediction': prediction.tolist(), 'diagnosis': diagnosis})

if __name__ == '__main__':
    app.run(debug=True)
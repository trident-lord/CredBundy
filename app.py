from flask import Flask, request, jsonify
import joblib
import sqlite3
from logger import log_transaction

app = Flask(__name__)

# Load the trained model
model = joblib.load('E:/CredBundy/backend/model/fraud_detection_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    transaction_details = data['transaction_details']
    transaction_features = data['features']

    # Predict fraud
    prediction = model.predict([transaction_features])[0]
    result = 'Fraud' if prediction == -1 else 'Legitimate'

    # Log transaction
    transaction_id = data.get('transaction_id', 'Unknown')
    log_transaction(transaction_id, transaction_details, result)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

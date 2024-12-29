import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
data = pd.read_csv('E:/CredBundy/datasets/creditcard.csv')

# Preprocess
X = data.drop(columns=['Class'])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = IsolationForest(n_estimators=100, random_state=42)
model.fit(X_scaled)

# Save model
joblib.dump(model, 'fraud_detection_model.pkl')

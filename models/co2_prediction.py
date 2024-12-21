"""
co2_prediction.py
-----------------
A simple linear regression model to predict CO2 emissions per route.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

class CO2Predictor:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, data):
        """
        Train a simple model to predict CO2 emissions.
        data is a pandas DataFrame containing the columns:
        ['distance_km', 'weight', 'base_co2_per_km', 'co2_emitted']
        """
        X = data[['distance_km', 'weight', 'base_co2_per_km']]
        y = data['co2_emitted']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        score = self.model.score(X_test, y_test)
        print(f"Model training complete. R^2 Score: {score:.2f}")

    def predict(self, distance_km, weight, base_co2_per_km):
        """
        Predict CO2 emissions for a single route.
        """
        return self.model.predict([[distance_km, weight, base_co2_per_km]])[0]

    def save_model(self, filename="co2_model.pkl"):
        joblib.dump(self.model, filename)

    def load_model(self, filename="co2_model.pkl"):
        self.model = joblib.load(filename)

if __name__ == "__main__":
    # Example usage
    # Create fake training data
    df = pd.read_csv("data/traindata.csv")
    """
    df = pd.DataFrame({
        "distance_km": [100, 200, 150, 300, 120],
        "weight": [200, 400, 300, 500, 250],
        "base_co2_per_km": [0.8, 0.9, 1.0, 0.7, 0.85],
        "co2_emitted": [160, 360, 300, 350, 255]  # Example target
    })
    """
    predictor = CO2Predictor()
    predictor.train(df)
    predictor.save_model()

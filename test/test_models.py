import pytest
import pandas as pd
from models.co2_prediction import CO2Predictor

def test_co2_prediction_train_predict():
    # Arrange
    df = pd.DataFrame({
        "distance_km": [100, 200, 150, 300, 120],
        "weight": [200, 400, 300, 500, 250],
        "base_co2_per_km": [0.8, 0.9, 1.0, 0.7, 0.85],
        "co2_emitted": [160, 360, 300, 350, 255]
    })
    predictor = CO2Predictor()

    # Act
    predictor.train(df)
    prediction = predictor.predict(150, 300, 0.9)

    # Assert
    assert prediction > 0, "Prediction should be positive"
    # Optionally check if it's within a plausible range
    assert 200 < prediction < 400, "Prediction should be within expected range"

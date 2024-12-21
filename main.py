"""
main.py
-------
Entry point for running the project.
"""

import pandas as pd
from models.co2_prediction import CO2Predictor
from optimization.route_optimizer import optimize_routes

def main():
    # Load data
    vehicles_df = pd.read_csv("data/vehicles.csv")
    routes_df = pd.read_csv("data/routes.csv")
    shipments_df = pd.read_csv("data/shipments.csv")

    # Train or load your CO2 model
    co2_model = CO2Predictor()
    try:
        co2_model.load_model("co2_model.pkl")
        print("Loaded existing CO2 model.")
    except:
        # If no saved model, train a new one (In practice, you might need labeled data with actual CO2)
        print("No saved model found. Training a new model on dummy data.")
        dummy_data = pd.DataFrame({
            "distance_km": [100, 200, 150, 300, 120],
            "weight": [200, 400, 300, 500, 250],
            "base_co2_per_km": [0.8, 0.9, 1.0, 0.7, 0.85],
            "co2_emitted": [160, 360, 300, 350, 255]  # Example target
        })
        co2_model.train(dummy_data)
        co2_model.save_model("co2_model.pkl")

    # Run optimization
    assignment = optimize_routes(vehicles_df, routes_df, shipments_df)
    print("Optimization Results:")
    for shipment, vehicle in assignment.items():
        print(f"  Shipment {shipment} assigned to {vehicle}")

if __name__ == "__main__":
    main()

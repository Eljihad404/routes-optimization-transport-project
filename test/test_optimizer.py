import pytest
import pandas as pd
from optimization.route_optimizer import optimize_routes

def test_optimize_routes_basic():
    # Arrange
    vehicles_df = pd.DataFrame({
        "vehicle_id": ["V1"],
        "vehicle_type": ["truck"],
        "max_capacity": [1000],
        "base_co2_per_km": [0.9]
    })
    routes_df = pd.DataFrame({
        "route_id": ["R1"],
        "origin": ["WarehouseA"],
        "destination": ["CityA"],
        "distance_km": [300]
    })
    shipments_df = pd.DataFrame({
        "shipment_id": ["S1"],
        "weight": [200],
        "required_origin": ["WarehouseA"],
        "required_destination": ["CityA"]
    })

    # Act
    assignment = optimize_routes(vehicles_df, routes_df, shipments_df)

    # Assert
    assert assignment["S1"] == "V1", "Shipment should be assigned to V1."

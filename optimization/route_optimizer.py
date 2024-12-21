"""
route_optimizer.py
------------------
Uses linear programming (PuLP or similar) to minimize CO2 emissions subject to
capacity constraints and required shipments.
"""

import pandas as pd
from pulp import LpMinimize, LpProblem, LpVariable, lpSum
from models.co2_prediction import CO2Predictor

def optimize_routes(vehicles_df, routes_df, shipments_df):
    """
    vehicles_df: DataFrame with columns [vehicle_id, vehicle_type, max_capacity, base_co2_per_km]
    routes_df:   DataFrame with columns [route_id, origin, destination, distance_km]
    shipments_df:DataFrame with columns [shipment_id, weight, required_origin, required_destination]
    
    Returns: A dictionary { "shipment_id": "vehicle_id" } indicating assignment.
    """

    # Initialize model
    problem = LpProblem("Minimize_CO2_Emissions", LpMinimize)

    # Create variables for each shipment-vehicle assignment (binary)
    # assignment[shipment_id, vehicle_id] = 1 if assigned, 0 otherwise
    assignment = {}
    for shipment_id in shipments_df['shipment_id']:
        for vehicle_id in vehicles_df['vehicle_id']:
            assignment[(shipment_id, vehicle_id)] = LpVariable(
                f"assign_{shipment_id}_{vehicle_id}", 
                cat="Binary"
            )

    # Initialize a CO2 predictor
    co2_model = CO2Predictor()
    # For demonstration, let's load a pre-trained model (if exists)
    try:
        co2_model.load_model()
    except:
        pass  # or co2_model.train(...) with your data

    # Objective: minimize total CO2 = sum of (distance_km * base_co2_per_km) * weight factor
    # We'll use the model's predicted emissions if available
    total_co2 = []
    for idx, shipment in shipments_df.iterrows():
        for jdx, vehicle in vehicles_df.iterrows():
            route_candidates = routes_df[
                (routes_df['origin'] == shipment['required_origin']) & 
                (routes_df['destination'] == shipment['required_destination'])
            ]
            if len(route_candidates) > 0:
                route = route_candidates.iloc[0]
                # Predict CO2 for that route with the vehicle
                predicted_co2 = co2_model.predict(
                    distance_km=route['distance_km'],
                    weight=shipment['weight'],
                    base_co2_per_km=vehicle['base_co2_per_km']
                )
                total_co2.append(predicted_co2 * assignment[(shipment['shipment_id'], vehicle['vehicle_id'])])
            else:
                # If there's no matching route, it can't be assigned, so it's effectively infinite or disallowed
                total_co2.append(9999999 * assignment[(shipment['shipment_id'], vehicle['vehicle_id'])])

    problem += lpSum(total_co2), "Total_CO2_Emissions"

    # Constraints
    # 1) Each shipment is assigned to exactly one vehicle
    for shipment_id in shipments_df['shipment_id']:
        problem += lpSum([assignment[(shipment_id, v)] for v in vehicles_df['vehicle_id']]) == 1

    # 2) Vehicle capacity constraints
    for vehicle_id in vehicles_df['vehicle_id']:
        vehicle_cap = vehicles_df[vehicles_df['vehicle_id'] == vehicle_id]['max_capacity'].values[0]
        # Sum of weights of shipments assigned to the vehicle <= max_capacity
        problem += lpSum([
            shipments_df[shipments_df['shipment_id'] == s]['weight'].values[0] * assignment[(s, vehicle_id)]
            for s in shipments_df['shipment_id']
        ]) <= vehicle_cap

    # Solve
    problem.solve()

    # Construct assignment dictionary
    shipment_assignment = {}
    for shipment_id in shipments_df['shipment_id']:
        for vehicle_id in vehicles_df['vehicle_id']:
            if assignment[(shipment_id, vehicle_id)].varValue == 1:
                shipment_assignment[shipment_id] = vehicle_id

    return shipment_assignment

if __name__ == "__main__":
    # Example usage
    vehicles_df = pd.read_csv("data/vehicles.csv")
    routes_df = pd.read_csv("data/routes.csv")
    shipments_df = pd.read_csv("data/shipments.csv")

    best_assignment = optimize_routes(vehicles_df, routes_df, shipments_df)
    print("Optimized Assignment:", best_assignment)

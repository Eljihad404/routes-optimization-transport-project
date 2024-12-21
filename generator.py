import pandas as pd
import random

def generate_vehicles(num_vehicles=100):
    vehicle_types = ["truck", "van", "bike", "electric_truck"]
    vehicles = []

    for i in range(1, num_vehicles + 1):
        vehicle_id = f"V{i}"
        vehicle_type = random.choice(vehicle_types)
        max_capacity = random.randint(200, 2000)  # Capacity between 200 and 2000
        base_co2_per_km = round(random.uniform(0.1, 1.5), 2)  # CO2 emissions

        vehicles.append({
            "vehicle_id": vehicle_id,
            "vehicle_type": vehicle_type,
            "max_capacity": max_capacity,
            "base_co2_per_km": base_co2_per_km
        })

    vehicles_df = pd.DataFrame(vehicles)
    vehicles_df.to_csv("data/vehicles.csv", index=False)
    print(f"Generated {num_vehicles} vehicles in data/vehicles.csv")

generate_vehicles(100)

def generate_routes(num_routes=300):
    locations = ["WarehouseA", "WarehouseB", "CityA", "CityB", "CityC", "CityD", "CityE"]
    routes = []

    for i in range(1, num_routes + 1):
        origin = random.choice(locations)
        destination = random.choice([loc for loc in locations if loc != origin])
        distance_km = random.randint(50, 1500)  # Random distance

        routes.append({
            "route_id": f"R{i}",
            "origin": origin,
            "destination": destination,
            "distance_km": distance_km
        })

    routes_df = pd.DataFrame(routes)
    routes_df.to_csv("data/routes.csv", index=False)
    print(f"Generated {num_routes} routes in data/routes.csv")

generate_routes(300)

def generate_shipments(num_shipments=500):
    origins = ["WarehouseA", "WarehouseB"]
    destinations = ["CityA", "CityB", "CityC", "CityD", "CityE"]
    shipments = []

    for i in range(1, num_shipments + 1):
        shipment_id = f"S{i}"
        weight = random.randint(50, 2000)  # Shipment weight between 50 and 2000
        origin = random.choice(origins)
        destination = random.choice(destinations)

        shipments.append({
            "shipment_id": shipment_id,
            "weight": weight,
            "required_origin": origin,
            "required_destination": destination
        })

    shipments_df = pd.DataFrame(shipments)
    shipments_df.to_csv("data/shipments.csv", index=False)
    print(f"Generated {num_shipments} shipments in data/shipments.csv")

generate_shipments(500)

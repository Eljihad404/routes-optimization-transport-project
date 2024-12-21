import csv
import random

def generate_fake_data(num_shipments=10):
    """Generates fake data for shipments, routes, and vehicles."""
    # Example of generating random shipments
    shipments = []
    for i in range(num_shipments):
        weight = random.randint(100, 1500)
        origin = random.choice(["WarehouseA", "WarehouseB"])
        destination = random.choice(["CityA", "CityB", "CityC"])
        shipments.append([f"S{i+1}", weight, origin, destination])
    
    # You could write them to CSV if needed:
    with open('data/shipments.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["shipment_id", "weight", "required_origin", "required_destination"])
        writer.writerows(shipments)

if __name__ == "__main__":
    # This script can be run independently to generate new data
    generate_fake_data(num_shipments=10)

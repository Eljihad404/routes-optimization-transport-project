import pandas as pd
import numpy as np

def generate_synthetic_data(num_samples=500, output_file="synthetic_data.csv"):
    """
    Generates a synthetic dataset for CO2 emissions.
    :param num_samples: Number of samples to generate
    :param output_file: Output file to save the generated dataset
    """
    np.random.seed(42)  # For reproducibility

    # Generate random distances (in km), weights (in kg), and base CO2 per km
    distances = np.random.randint(50, 1500, num_samples)  # Distances between 50 and 1500 km
    weights = np.random.randint(100, 2000, num_samples)   # Weights between 100 and 2000 kg
    base_co2_per_km = np.random.uniform(0.5, 1.5, num_samples)  # CO2 rate between 0.5 and 1.5 kg/km

    # Calculate CO2 emitted with some randomness to simulate real-world variability
    co2_emitted = distances * weights * base_co2_per_km / 1000  # CO2 in kilograms
    co2_emitted += np.random.normal(0, 10, num_samples)  # Adding some noise

    # Create a DataFrame
    data = pd.DataFrame({
        "distance_km": distances,
        "weight": weights,
        "base_co2_per_km": base_co2_per_km,
        "co2_emitted": co2_emitted
    })

    # Save to a CSV file
    data.to_csv("data/traindata.csv", index=False)

# Generate the dataset
generate_synthetic_data()

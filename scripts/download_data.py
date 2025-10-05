import urllib.request
import os

# Download the medical examination dataset
url = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-medical-data-visualizer/master/medical_examination.csv'
filename = 'medical_examination.csv'

print(f"Downloading medical examination data from freeCodeCamp...")

try:
    urllib.request.urlretrieve(url, filename)
    print(f"✓ Successfully downloaded {filename}")
    print(f"✓ File size: {os.path.getsize(filename)} bytes")
except Exception as e:
    print(f"✗ Error downloading file: {e}")
    print("\nCreating sample data for demonstration...")
    
    # Create sample data if download fails
    import pandas as pd
    import numpy as np
    
    np.random.seed(42)
    n_samples = 70000
    
    sample_data = pd.DataFrame({
        'id': range(n_samples),
        'age': np.random.randint(10000, 25000, n_samples),
        'height': np.random.randint(140, 200, n_samples),
        'weight': np.random.uniform(40, 120, n_samples),
        'gender': np.random.choice([1, 2], n_samples),
        'ap_hi': np.random.randint(90, 180, n_samples),
        'ap_lo': np.random.randint(60, 120, n_samples),
        'cholesterol': np.random.choice([1, 2, 3], n_samples, p=[0.6, 0.3, 0.1]),
        'gluc': np.random.choice([1, 2, 3], n_samples, p=[0.7, 0.2, 0.1]),
        'smoke': np.random.choice([0, 1], n_samples, p=[0.9, 0.1]),
        'alco': np.random.choice([0, 1], n_samples, p=[0.95, 0.05]),
        'active': np.random.choice([0, 1], n_samples, p=[0.2, 0.8]),
        'cardio': np.random.choice([0, 1], n_samples, p=[0.5, 0.5])
    })
    
    sample_data.to_csv(filename, index=False)
    print(f"✓ Created sample {filename} with {n_samples} records")

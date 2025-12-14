import numpy as np
import pandas as pd
import time

def mock_oracle(is_leak):
    # Base latency 20ms, Jitter 2ms (Normal Distribution)
    base = 20 + np.random.normal(0, 2)
    if is_leak:
        # Add 6ms leak
        base += 6
    return base

def run_test():
    print("Generating raw traces for analysis...")
    n_samples = 1000
    
    # Generate Synthetic Data
    np.random.seed(42) # Reproducibility
    control_times = [mock_oracle(False) for _ in range(n_samples)]
    leak_times = [mock_oracle(True) for _ in range(n_samples)]
    
    # Save to CSV
    pd.DataFrame(control_times, columns=['latency']).to_csv('control_trace.csv', index=False)
    pd.DataFrame(leak_times, columns=['latency']).to_csv('leak_trace.csv', index=False)
    print(f"Saved {n_samples} samples to control_trace.csv and leak_trace.csv")

if __name__ == "__main__":
    run_test()

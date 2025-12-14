import time
from vulnerable_regex import handle_request
import matplotlib.pyplot as plt

def measure_redos():
    lengths = range(1, 25)
    durations = []
    
    print("Benchmarking ReDoS Vulnerability...")
    print(f"{'Input Length':<15} | {'Duration (ms)':<15}")
    print("-" * 35)
    
    for n in lengths:
        # Construct evil input: n 'a's followed by a non-matching character
        payload = ("a" * n) + "X"
        
        response = handle_request({"input": payload})
        duration = response["duration_ms"]
        durations.append(duration)
        
        print(f"{n:<15} | {duration:.4f}")

    # Check for exponential growth characteristic of ReDoS
    if durations[-1] > durations[0] * 10:
        print("\n[+] ReDoS Vulnerability Confirmed: Exponential timing growth detected!")
    else:
        print("\n[-] No significant timing leak detected.")

if __name__ == "__main__":
    measure_redos()

import time
import random
import string
from constant_time_compare import constant_time_compare, naive_compare

def measure_time(func, s1, s2, iterations=100000):
    start = time.time_ns()
    for _ in range(iterations):
        func(s1, s2)
    end = time.time_ns()
    return (end - start) / iterations

def run_benchmark():
    password = "SuperSecretPassword123!"
    # Case 1: First char mismatch (Fastest for naive)
    wrong_start = "A" + password[1:]
    # Case 2: Last char mismatch (Slowest for naive)
    wrong_end = password[:-1] + "X"
    
    print(f"Benchmarking (N=100k iterations)...")
    print("-" * 60)
    print(f"{'Method':<20} | {'First-Char-Diff (ns)':<20} | {'Last-Char-Diff (ns)':<20} | {'Diff'}")
    print("-" * 60)
    
    # Test Naive
    t_naive_fast = measure_time(naive_compare, password, wrong_start)
    t_naive_slow = measure_time(naive_compare, password, wrong_end)
    diff_naive = t_naive_slow - t_naive_fast
    
    print(f"{'Naive (Vulnerable)':<20} | {t_naive_fast:>20.2f} | {t_naive_slow:>20.2f} | {diff_naive:>5.2f} ns")

    # Test Constant Time
    t_safe_fast = measure_time(constant_time_compare, password, wrong_start)
    t_safe_slow = measure_time(constant_time_compare, password, wrong_end)
    diff_safe = t_safe_slow - t_safe_fast

    print(f"{'Constant-Time (Safe)':<20} | {t_safe_fast:>20.2f} | {t_safe_slow:>20.2f} | {diff_safe:>5.2f} ns")
    print("-" * 60)
    
    if abs(diff_safe) < 100: # Allow small jitter
        print("[+] SUCCESS: Constant-time comparison eliminated the timing leak!")
    else:
        print("[-] WARNING: Timing difference still detected (check noise).")

if __name__ == "__main__":
    run_benchmark()

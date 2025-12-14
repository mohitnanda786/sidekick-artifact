import time
import numpy as np
from scipy import stats
from sidekick.utils.logger import logger

class TimingOracle:
    def __init__(self, target_function):
        """
        :param target_function: A callable that takes a string/bytes input 
                                and performs the operation to be measured.
        """
        self.target_function = target_function

    def measure(self, input_val: str, iterations: int = 100) -> float:
        """Measure average execution time for a given input."""
        times = []
        for _ in range(iterations):
            start = time.perf_counter()
            self.target_function(input_val)
            end = time.perf_counter()
            times.append(end - start)
        return float(np.mean(times))

    def detect_leak(self, good_inputs: list, bad_inputs: list) -> dict:
        """
        Perform a Welch's t-test to detect statistically significant timing differences.
        """
        logger.info(f"Collecting samples for {len(good_inputs)} good inputs and {len(bad_inputs)} bad inputs...")
        
        good_times = []
        bad_times = []

        # Collect raw samples (can be optimized to parallelize)
        for inp in good_inputs:
            start = time.perf_counter()
            self.target_function(inp)
            good_times.append(time.perf_counter() - start)
            
        for inp in bad_inputs:
            start = time.perf_counter()
            self.target_function(inp)
            bad_times.append(time.perf_counter() - start)

        t_stat, p_val = stats.ttest_ind(good_times, bad_times, equal_var=False)
        
        is_leak = p_val < 0.001  # Threshold
        
        result = {
            "mean_good": np.mean(good_times),
            "mean_bad": np.mean(bad_times),
            "diff": np.mean(good_times) - np.mean(bad_times),
            "p_value": p_val,
            "is_leak": is_leak
        }
        
        logger.info(f"Oracle Result: Leak={'YES' if is_leak else 'NO'} (p={p_val:.2e})")
        return result

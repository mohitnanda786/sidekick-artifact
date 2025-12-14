import subprocess
import os
import signal
import time
from typing import List, Optional
from sidekick.utils.logger import logger

class AFLWrapper:
    def __init__(self, input_dir: str, output_dir: str, target_cmd: List[str]):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.target_cmd = target_cmd
        self.process: Optional[subprocess.Popen] = None

    def start(self, timeout: int = None):
        """Start the AFL++ fuzzer instance."""
        cmd = [
            "afl-fuzz",
            "-i", self.input_dir,
            "-o", self.output_dir,
            "-D" # Deterministic mode usually good for side-channels initially
        ] + ["--"] + self.target_cmd

        logger.info(f"Starting AFL++: {' '.join(cmd)}")
        
        # Ensure directories exist
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

        try:
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            if timeout:
                time.sleep(timeout)
                self.stop()
                
        except FileNotFoundError:
            logger.error("afl-fuzz not found. Ensure it is installed and in PATH.")

    def stop(self):
        """Stop the fuzzer."""
        if self.process:
            logger.info("Stopping AFL++...")
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
            logger.info("AFL++ stopped.")

    def get_stats(self):
        """Read fuzzer_stats file."""
        stats_file = os.path.join(self.output_dir, "default", "fuzzer_stats")
        if not os.path.exists(stats_file):
            return {}
        
        stats = {}
        with open(stats_file, 'r') as f:
            for line in f:
                if ":" in line:
                    key, val = line.strip().split(":", 1)
                    stats[key.strip()] = val.strip()
        return stats

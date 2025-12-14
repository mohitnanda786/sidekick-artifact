import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def simulate_arch_variance():
    """
    Simulates SideKick detection on:
    1. Intel Xeon (x86_64) - CISC, Hyperthreading noise, complex power management.
    2. AWS Graviton3 (ARM64) - RISC, physical cores (no SMT), predictable timing.
    
    Hypothesis: ARM64 has LOWER variance, making leaks EASIER to detect.
    """
    n_samples = 1000
    leak_magnitude = 0.5 # ms (Very small leak)
    
    # 1. x86_64 (Intel Xeon)
    # High variance due to Hyperthreading resource sharing and outdated microcode patches
    x86_noise_std = 4.0 
    x86_base = 20.0
    x86_control = np.random.normal(x86_base, x86_noise_std, n_samples)
    x86_leak = np.random.normal(x86_base + leak_magnitude, x86_noise_std, n_samples)
    
    # 2. ARM64 (Graviton3)
    # Lower variance: No Hyperthreading (1 vCPU = 1 Physical Core), simpler pipeline.
    arm_noise_std = 1.5
    arm_base = 18.0 # Slightly faster
    arm_control = np.random.normal(arm_base, arm_noise_std, n_samples)
    arm_leak = np.random.normal(arm_base + leak_magnitude, arm_noise_std, n_samples)
    
    # Stats
    _, p_x86 = stats.ttest_ind(x86_control, x86_leak)
    _, p_arm = stats.ttest_ind(arm_control, arm_leak)
    
    print(f"Architecture Simulation (Leak = {leak_magnitude}ms)")
    print(f"x86 (Intel) p-value: {p_x86:.4f} (Detected? {p_x86 < 0.05})")
    print(f"ARM (Graviton) p-value: {p_arm:.4f} (Detected? {p_arm < 0.05})")
    
    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # x86
    ax1.hist(x86_control, bins=30, alpha=0.5, label='Match', color='gray')
    ax1.hist(x86_leak, bins=30, alpha=0.5, label='Mismatch', color='red')
    ax1.set_title(f"Intel Xeon (x86)\nHigh Noise (p={p_x86:.2f})")
    ax1.set_xlabel("Time (ms)")
    ax1.legend()
    
    # ARM
    ax2.hist(arm_control, bins=30, alpha=0.5, label='Match', color='gray')
    ax2.hist(arm_leak, bins=30, alpha=0.5, label='Mismatch', color='green')
    ax2.set_title(f"AWS Graviton (ARM64)\nLow Noise (p={p_arm:.2e})")
    ax2.set_xlabel("Time (ms)")
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('arch_comparison.png')
    print("Plot saved to arch_comparison.png")

if __name__ == "__main__":
    simulate_arch_variance()

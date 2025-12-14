# SideKick Artifact

This repository contains the artifacts for the paper **"SideKick: Hybrid Detection of Timing Side-Channels in Serverless Python via Symbolic Solving and Statistical Oracles"**.

## Contents

- `src/`: Source code for the SideKick fuzzer and oracle.
- `examples/`: Vulnerable serverless functions (benchmarks).
- `experiments/`: Scripts used for evaluation (jitter simulation, power analysis).
- `Dockerfile`: Environment definition.

## Getting Started

### Prerequisites

- Docker
- Python 3.12 (optional, for local run)

### Build Docker Image

```bash
docker build -t sidekick-artifact:v1.0 .
```

### Reproduce Results

**1. Figure 4: Power Sensitivity Analysis**
```bash
docker run --rm -v $(pwd):/work sidekick-artifact:v1.0 bash run_fig4.sh
```
Output: `power_sensitivity.png`

**2. Table 1: ReDoS Timing**
```bash
docker run --rm -v $(pwd):/work sidekick-artifact:v1.0 bash run_table1.sh
```
Output: Console table showing timing growth.

## Manual Usage

To run the fuzzer on the example target:

```bash
docker run --rm -it -v $(pwd):/work sidekick-artifact:v1.0 bash
# Inside container:
python -m sidekick.cli run --target examples/fake_lambda.py --duration 600
```

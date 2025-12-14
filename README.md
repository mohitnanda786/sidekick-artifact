# SideKick Artifact
[![Tested On](https://img.shields.io/badge/Tested%20On-Ubuntu%2020.04%20%7C%20Docker-blue)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

This repository contains the artifacts for the paper **"SideKick: Hybrid Detection of Timing Side-Channels in Serverless Python via Symbolic Solving and Statistical Oracles"** (IEEE Transactions).

## Contents
- `src/`: Source code for the SideKick fuzzer and oracle.
- `examples/`: Vulnerable serverless functions (benchmarks).
- `experiments/`: Evaluation scripts (jitter simulation, power analysis).
- `Dockerfile`: Environment definition.

## Quick Start
b
### 1. Build
```bash
docker build -t sidekick-artifact:v1.0 .
```

### 2. Verify (Reproduce Figure 4)
```bash
docker run --rm -v $(pwd):/work sidekick-artifact:v1.0 bash run_fig4.sh
```

### 3. Fuzz (Interactive)
```bash
docker run --rm -it -v $(pwd):/work sidekick-artifact:v1.0 bash
# Inside container:
python -m sidekick.cli run --target examples/fake_lambda.py --duration 600
```

## Citation
If you use SideKick, please cite:
```bibtex
@article{sidekick2025,
  title={SideKick: Hybrid Detection of Timing Side-Channels in Serverless Python},
  author={Nanda, Mohit et al.},
  journal={IEEE Transactions on Software Engineering},
  year={2025}
}
```

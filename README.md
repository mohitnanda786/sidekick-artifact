# SideKick Artifact
[![Tested On](https://img.shields.io/badge/Tested%20On-Ubuntu%2020.04%20%7C%20Docker-blue)](https://www.docker.com/)

This repository contains the research artifact for **SideKick: Hybrid Detection of Timing Side-Channels in Serverless Python via Symbolic Solving and Statistical Oracles**, a paper in preparation (not yet published).

## Contents
- `src/`: Source code for the SideKick fuzzer and oracle.
- `examples/`: Vulnerable serverless functions (benchmarks).
- `experiments/`: Evaluation scripts (jitter simulation, power analysis).
- `Dockerfile`: Environment definition.

## Quick Start
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
The paper has not been published yet. Citation details will be added here once it is. Until then, please cite this repository:
```bibtex
@misc{sidekick-artifact,
  title={SideKick: Hybrid Detection of Timing Side-Channels in Serverless Python (research artifact)},
  author={Nanda, Mohit and others},
  howpublished={\url{https://github.com/mohitnanda786/sidekick-artifact}},
  note={Paper in preparation},
  year={2025}
}
```

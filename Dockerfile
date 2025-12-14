FROM python:3.12-slim-bookworm

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl wget stress-ng build-essential clang llvm llvm-dev lld \
    libglib2.0-dev libpixman-1-dev \
    python3-dev \
    flex bison \
    && rm -rf /var/lib/apt/lists/*

# Build AFL++ from source
WORKDIR /tmp
RUN git clone https://github.com/AFLplusplus/AFLplusplus && \
    cd AFLplusplus && \
    make source-only && \
    make install && \
    cd .. && rm -rf AFLplusplus

# Install Python dependencies
# Removed 'afl' as it's not a valid PyPI package. 
# 'atheris' is the modern python fuzzer, and we can use 'python-afl' if strictly needed, 
# but for this build we will rely on atheris/manual wrappers.
RUN pip install --no-cache-dir \
    localstack boto3 scipy pingouin angr atheris poetry click rich pyyaml numpy matplotlib

# Set paths
ENV PYTHONPATH=/workspace/src
WORKDIR /workspace

# Copy project files
COPY . /workspace

# Default command
CMD ["bash"]

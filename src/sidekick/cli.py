import click
import os
import sys

# Add src to path so imports work
sys.path.append(os.path.join(os.getcwd(), "src"))

from sidekick.orchestrator import Orchestrator
from sidekick.utils.logger import logger

@click.group()
def cli():
    """SideKick: Hybrid Side-Channel Detection Framework"""
    pass

@cli.command()
@click.option("--target", required=True, help="Target Python script")
@click.option("--input-dir", default="inputs", help="Seed input directory")
@click.option("--output-dir", default="outputs", help="AFL output directory")
@click.option("--duration", default=60, help="Fuzzing duration in seconds")
def run(target, input_dir, output_dir, duration):
    """Run the SideKick detection loop."""
    logger.info(f"Initializing SideKick for target: {target}")
    orch = Orchestrator(target, input_dir, output_dir)
    orch.run(duration=duration)

if __name__ == "__main__":
    cli()

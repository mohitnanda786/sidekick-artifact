import logging
from rich.logging import RichHandler

def setup_logger(name="sidekick", level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )
    return logging.getLogger(name)

logger = setup_logger()

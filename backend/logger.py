import logging
import sys

# Create a custom logger
logger = logging.getLogger("forge_api")
logger.setLevel(logging.INFO) # We want to capture INFO, WARNING, ERROR, and CRITICAL

# Create handlers (where the logs will go - in this case, the terminal)
console_handler = logging.StreamHandler(sys.stdout)

# Create a formatter (how the logs will look)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(formatter)

# Add the handler to the logger
if not logger.handlers:
    logger.addHandler(console_handler)
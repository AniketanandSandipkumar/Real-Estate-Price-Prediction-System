import logging
import os

# Create logs directory if not exists
os.makedirs("backend/logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="backend/logs/api_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create custom logger
logger = logging.getLogger(__name__)

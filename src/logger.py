import logging # In-built module 
import os # In-built module
from datetime import datetime # In-built module

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)


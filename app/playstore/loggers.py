from datetime import datetime
from config import LOGS_NAME_DATE_FORMAT, LOGS_PLAYSTORE_FOLDER
from logs_handler import setup_logger

current_date = datetime.now().strftime(LOGS_NAME_DATE_FORMAT)
logger = setup_logger(name="playstore_logger", log_file=f"{LOGS_PLAYSTORE_FOLDER}{current_date}.log")

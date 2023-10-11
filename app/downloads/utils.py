import json

from app.downloads.loggers import logger
from app.downloads.schema import DownloadsSchema
from config import DOWNLOAD_FILE_PATH
from error_utils import ValidatorService


def open_json_file(file_path: str) -> dict:
    """Open a json file and returns its content as a dict"""
    data = None
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except Exception as e:
        print(f"Exception while opening file: {e}")
    return data


def validate_json_file(file_path: str) -> None:
    """Validate a json file against the schema."""
    data = open_json_file(file_path)
    validator_service = ValidatorService(DownloadsSchema, logger)

    validator_service.check_and_count_mismatches(data)
    validator_service.print_incorrect_columns()
    validator_service.print_missing_columns()


if __name__ == "__main__":
    validate_json_file(DOWNLOAD_FILE_PATH)

import json

from app.downloads.schema import DownloadsSchema
from config import DOWNLOAD_FILE_PATH
from error_utils import check_and_count_mismatches, print_validation_results


def open_data_file(file_path: str) -> dict:
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
    data = open_data_file(file_path)
    missing_columns_errors, wrong_type_errors = check_and_count_mismatches(data, schema_class=DownloadsSchema)
    print_validation_results(missing_columns_errors, wrong_type_errors)


if __name__ == "__main__":
    validate_json_file(DOWNLOAD_FILE_PATH)

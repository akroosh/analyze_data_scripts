import json
from collections import defaultdict
from typing import Any, Tuple

from app.downloads.schema import DownloadsSchema
from pydantic import ValidationError
from config import DOWNLOAD_FILE_PATH


def open_data_file(file_path: str) -> dict:
    """Open a json file and returns its content as a dict"""
    data = None
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except Exception as e:
        print(f"Exception while opening file: {e}")
    return data


def is_missing_column(error: dict[str, Any]) -> bool:
    """Check if the error is a missing column error."""
    return not error["input"] or error["type"] == "missing"


def print_results(missing_columns_errors: dict[str, int], wrong_type_errors: dict[str, int]) -> None:
    """Print the results of the validation."""
    if missing_columns_errors:
        for column, count in missing_columns_errors.items():
            print(f"Missing column `{column}`: {count} times")
    if wrong_type_errors:
        for column, count in wrong_type_errors.items():
            print(f"Wrong column `{column}`: {count} times")


def check_and_count_mismatches(data: dict) -> Tuple[dict[str, int], dict[str, int]]:
    """Check if the data matches the schema and count the errors."""
    missing_columns_errors = defaultdict(lambda: 0)
    wrong_type_errors = defaultdict(lambda: 0)
    try:
        DownloadsSchema(**data)
    except ValidationError as e:
        for error in e.errors():
            column = error["loc"][0]
            if is_missing_column(error):
                missing_columns_errors[column] += 1
            else:
                wrong_type_errors[column] += 1
    return missing_columns_errors, wrong_type_errors


def validate_json_file(file_path: str) -> None:
    """Validate a json file against the schema."""
    data = open_data_file(file_path)
    missing_columns_errors, wrong_type_errors = check_and_count_mismatches(data)
    print_results(missing_columns_errors, wrong_type_errors)


if __name__ == "__main__":
    validate_json_file(DOWNLOAD_FILE_PATH)

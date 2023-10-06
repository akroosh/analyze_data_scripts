import json
from collections import defaultdict

from schema import DownloadsSchema
from pydantic import ValidationError
from config import DOWNLOAD_FILE_PATH


def open_data_file(file_path: str):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

    except Exception as e:
        print(f"Exception while opening file: {e}")
        data = None

    return data


def check_and_count_mismatches(data: dict):
    missing_columns_errors = defaultdict(lambda: 0)
    wrong_type_errors = defaultdict(lambda: 0)
    try:
        DownloadsSchema(**data)
    except ValidationError as e:
        for error in e.errors():
            column = error["loc"][0]
            if not error["input"] or error["type"] == "missing":
                missing_columns_errors[column] += 1
            else:
                wrong_type_errors[column] += 1

    print("missing fields:", dict(missing_columns_errors), "wrong types:", dict(wrong_type_errors))


if __name__ == "__main__":
    data = open_data_file(DOWNLOAD_FILE_PATH)
    check_and_count_mismatches(data)

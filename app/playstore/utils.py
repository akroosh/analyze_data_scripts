from collections import defaultdict
from typing import Tuple

import pandas as pd
from config import PLAYSTORE_FILE_PATH
from error_utils import print_validation_results, check_and_count_mismatches
from app.playstore.schema import SchemaValidator


def sum_all_dataframe_errors(results: pd.Series) -> Tuple[dict[str, int], dict[str, int]]:
    """Sum all the errors of a dataframe."""
    missing_columns_errors = defaultdict(lambda: 0)
    wrong_type_errors = defaultdict(lambda: 0)

    for row_missing_columns_errors, row_wrong_type_errors in results.to_list():

        for column, error_counter in row_missing_columns_errors.items():
            missing_columns_errors[column] += error_counter
        for column, error_counter in row_wrong_type_errors.items():
            wrong_type_errors[column] += error_counter
    return missing_columns_errors, wrong_type_errors


def find_and_print_null_values_df(df: pd.DataFrame) -> None:
    """Find and print the null values of a dataframe."""
    null_values = df.isnull().sum()
    print("Null values for each field:")
    print(null_values)


def check_data_types(df: pd.DataFrame) -> Tuple[dict[str, int], dict[str, int]]:
    """Check the data types of a dataframe."""
    results = df.apply(check_and_count_mismatches, axis=1, schema_class=SchemaValidator)
    missing_columns_errors, wrong_type_errors = sum_all_dataframe_errors(results)
    return missing_columns_errors, wrong_type_errors


def validate_json_file(file_path: str) -> None:
    """Validate a json file against the schema."""
    df = pd.read_json(file_path, lines=True)
    missing_columns_errors, wrong_type_errors = check_data_types(df)
    find_and_print_null_values_df(df)
    print_validation_results(missing_columns_errors, wrong_type_errors)


if __name__ == "__main__":
    validate_json_file(PLAYSTORE_FILE_PATH)

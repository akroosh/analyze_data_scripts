from collections import defaultdict
from typing import Any, Tuple

from pydantic import ValidationError, BaseModel


def is_missing_column(error: dict[str, Any]) -> bool:
    """Check if the error is a missing column error."""
    return not error["input"] or error["type"] == "missing"


def check_and_count_mismatches(data: dict, schema_class: BaseModel) -> Tuple[dict[str, int], dict[str, int]]:
    """Check if the data matches the schema and count the errors."""
    missing_columns_errors = defaultdict(lambda: 0)
    wrong_type_errors = defaultdict(lambda: 0)
    try:
        schema_class(**data)
    except ValidationError as e:
        for error in e.errors():
            column = error["loc"][0]
            if is_missing_column(error):
                missing_columns_errors[column] += 1
            else:
                wrong_type_errors[column] += 1
    return missing_columns_errors, wrong_type_errors


def check_row_and_print_results(
        data: dict, schema_class: BaseModel, row_number: int
) -> Tuple[dict[str, int], dict[str, int]]:
    """Check if the data in row matches the schema and print the results."""

    print(f"Row: {row_number}")
    print("-" * 20)
    missing_columns_errors, wrong_type_errors = check_and_count_mismatches(data, schema_class)
    print_validation_results(missing_columns_errors, wrong_type_errors)
    return missing_columns_errors, wrong_type_errors


def print_validation_results(missing_columns_errors: dict[str, int], wrong_type_errors: dict[str, int]) -> None:
    """Print the results of the validation."""
    if missing_columns_errors:
        for column, count in missing_columns_errors.items():
            print(f"Missing column `{column}`: {count} times")
    if wrong_type_errors:
        for column, count in wrong_type_errors.items():
            print(f"Wrong column `{column}`: {count} times")
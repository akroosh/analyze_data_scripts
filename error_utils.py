from collections import defaultdict
from enum import Enum
from logging import Logger
from typing import Any

from pydantic import ValidationError


class ValidatorService:
    class ErrorType(Enum):
        missing = "missing"
        value_error = "value_error"
        incorrect = "incorrect"

    def __init__(self, validator_class, logger: Logger):
        self.validator_class = validator_class

        self.missing_columns_errors = defaultdict(lambda: 0)
        self.incorrect_type_errors = defaultdict(lambda: 0)
        self.custom_errors = defaultdict(lambda: 0)

        self.logger = logger

    @classmethod
    def is_missing_column(cls, error: dict[str, Any]) -> bool:
        """Check if the error is a missing column error."""
        return not error["input"] or error["type"] == cls.ErrorType.missing.value

    def handle_error(self, error: ValidationError):
        """Find error column, type and calculate total errors values."""

        column = "__".join([str(loc) for loc in error["loc"]])

        if self.is_missing_column(error):
            self.missing_columns_errors[column] += 1
        else:
            self.incorrect_type_errors[column] += 1

    def check_and_count_mismatches(self, data: dict):
        """Check if the data matches the schema and count the errors."""
        try:
            self.validator_class(**data)
        except ValidationError as e:
            for error in e.errors():
                self.handle_error(error)

    def check_row_and_print_results(self, data: dict, row_number: int):
        """Check if the data in row matches the schema and print the results."""

        self.check_and_count_mismatches(data)
        self.print_missing_columns(row_number=row_number)
        self.print_incorrect_columns(row_number=row_number)

    def print_missing_columns(self, **kwargs) -> None:
        """Log the results of the missing columns validation."""
        for column, error_count in self.missing_columns_errors.items():
            self.logger.error({
                "column": column, "error_type": self.ErrorType.missing.value, "total_error_count": error_count, **kwargs
            })

    def print_incorrect_columns(self, **kwargs) -> None:
        """Log the results of the wrong columns validation."""
        for column, error_count in self.incorrect_type_errors.items():
            self.logger.error({
                "column": column, "error_type": self.ErrorType.incorrect.value, "total_error_count": error_count, **kwargs
            })

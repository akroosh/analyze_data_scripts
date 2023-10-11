import jsonlines
from app.playstore.loggers import logger
from app.playstore.schema import SchemaValidator
from error_utils import ValidatorService


def validate_jsonl(file_path):
    """Validate a jsonl file against the schema."""
    validator_service = ValidatorService(SchemaValidator, logger)
    with jsonlines.open(file_path) as reader:
        for row_number, line in enumerate(reader, start=1):
            validator_service.check_row_and_print_results(row_number=row_number, data=line)

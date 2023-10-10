import jsonlines

from app.playstore.schema import SchemaValidator
from error_utils import check_row_and_print_results


def validate_jsonl(file_path):
    """Validate a jsonl file against the schema."""
    with jsonlines.open(file_path) as reader:
        for row_number, line in enumerate(reader, start=1):
            check_row_and_print_results(row_number=row_number, data=line, schema_class=SchemaValidator)

from collections import defaultdict

import pandas as pd
from pandas import Series
from pydantic_core._pydantic_core import ValidationError

from config import PLAYSTORE_FILE_PATH
from app.playstore.schema import SchemaValidator


def check_data_types(df):
    def check_and_count_mismatches(row: Series):
        missing_columns_errors = defaultdict(lambda: 0)
        wrong_type_errors = defaultdict(lambda: 0)
        try:
            SchemaValidator(**row)
        except ValidationError as e:
            for error in e.errors():
                column = error["loc"][0]
                if error["type"] == "missing":
                    missing_columns_errors[column] += 1
                else:
                    wrong_type_errors[column] += 1
            print("missing fields:", dict(missing_columns_errors), "wrong types:", dict(wrong_type_errors))

    df.apply(check_and_count_mismatches, axis=1)

    null_values = df.isnull().sum()
    print("null values for each field:", null_values)


if __name__ == "__main__":
    df = pd.read_json(PLAYSTORE_FILE_PATH, lines=True)

    check_data_types(df)

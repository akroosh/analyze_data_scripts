from app.playstore.utils import check_data_types
from app.downloads.utils import validate_json_file
from config import PLAYSTORE_FILE_PATH, DOWNLOAD_FILE_PATH
import pandas as pd

if __name__ == "__main__":
    df = pd.read_json(PLAYSTORE_FILE_PATH, lines=True)
    check_data_types(df)

    validate_json_file(DOWNLOAD_FILE_PATH)

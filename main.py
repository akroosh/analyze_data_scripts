from app.playstore.utils import validate_jsonl as playstore_validate
from app.downloads.utils import validate_json_file as downloads_validate
from config import PLAYSTORE_FILE_PATH, DOWNLOAD_FILE_PATH

if __name__ == "__main__":
    print(f"Validating `{PLAYSTORE_FILE_PATH}`")
    playstore_validate(PLAYSTORE_FILE_PATH)
    print("-"*100)
    print(f"Validating `{DOWNLOAD_FILE_PATH}`")
    downloads_validate(DOWNLOAD_FILE_PATH)

from app.playstore.utils import validate_jsonl as playstore_validate
from app.downloads.utils import validate_json_file as downloads_validate
from config import PLAYSTORE_FILE_PATH, DOWNLOAD_FILE_PATH, LOGS_PLAYSTORE_FOLDER, LOGS_DOWNLOAD_FOLDER

if __name__ == "__main__":
    print(f"Validating `{PLAYSTORE_FILE_PATH}`")
    playstore_validate(PLAYSTORE_FILE_PATH)
    print(f"Validating `{DOWNLOAD_FILE_PATH}`")
    downloads_validate(DOWNLOAD_FILE_PATH)
    print(f"Finished validation. "
          f"You can find results in the `{LOGS_PLAYSTORE_FOLDER}` and `{LOGS_DOWNLOAD_FOLDER}` folders")

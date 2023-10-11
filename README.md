# Data analyzing scripts

## Overview
This project aims to read JSON files and identify both data and schema errors or inconsistencies.
The primary entry point for the project is `main.py`.
The project uses [Poetry](https://python-poetry.org/) for environment management,
and an alternative environment setup is available using the `requirements.txt` file.


## Setup Instructions

### Poetry Setup
1. Install Poetry if not already installed:
    ```bash
    pip install poetry
    ```

2. Navigate to the project directory and run:
    ```bash
    poetry install
    ```

3. Activate the virtual environment created by Poetry:
    ```bash
    poetry shell
    ```

### Alternative Setup (using `requirements.txt`)
1. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project
Execute the following command to start the project:
```bash
python main.py
```


## Logging
Results of each execution are logged in the `logs/filename` folder.
Log files are named with the date and time of execution, following the format specified in the `LOGS_NAME_DATE_FORMAT` variable in the `config.py` file which you can change.

Existing results files can be found in the `logs/filename` folder.
For example, a sample log files has been provided in the repository for reference.


## Configuring File Names
File names for utility files are configured in config.py.


Feel free to reach out if you have any questions or need further assistance!

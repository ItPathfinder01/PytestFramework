import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
TEST_DATA_DIR = BASE_DIR.joinpath('TestData')

def getJsonFromFile(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        return json.load(file)
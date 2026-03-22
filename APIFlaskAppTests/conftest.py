import pytest
from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.myconfigparser import getFlaskAppBaseURL

loginJsonFile = "loginValid.json"
baseURI = getFlaskAppBaseURL()
loginURLPath = "login"
usersURLPath = "users"
@pytest.fixture
def get_token():
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    response = postApiData(loginURL, payload)
    token = response.json()["token"]
    yield token

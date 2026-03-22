import json
import pytest
from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.myconfigparser import getFlaskAppBaseURL

# loginJsonFile = "loginValid.json"
baseURI = getFlaskAppBaseURL()
# loginURLPath = "login"
usersURLPath = "users"

# @pytest.fixture
# def get_token():
#     loginURL = baseURI + loginURLPath
#     payload = getJsonFromFile(loginJsonFile)
#     response = postApiData(loginURL, payload)
#     token = response.json()["token"]
#     yield token

# Test get users with fixtures
def test_getUsers(get_token):
    token = get_token
    usersURL = baseURI + usersURLPath
    headers = {"x-access-token": token}
    respUsers = getApiData(usersURL, headers)
    print(json.dumps(respUsers.json(), indent=4))
    assert respUsers.json()["users"][0][0]["email"] == "admin@admin"


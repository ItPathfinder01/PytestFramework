from utils.fileUtils import getJsonFromFile
from utils.apiUtils import postApiData, getApiData
from utils.myconfigparser import getFlaskAppBaseURL

loginJsonFile = "loginValid.json"
baseURI = getFlaskAppBaseURL()
loginURLPath = "login"
usersURLPath = "users"

# Demo test with token
def test_GetUsersDemo():
    # First login with an existing user
    loginURL = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    response = postApiData(loginURL, payload)
    print(response.json()["token"])
    token = response.json()["token"]
    userURL = baseURI + usersURLPath
    headers = {"x-access-token": token}
    response_users = getApiData(userURL, headers)
    print(response_users.json())



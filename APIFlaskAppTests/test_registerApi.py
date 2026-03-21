import requests

from utils.apiUtils import postApiData
from utils.fileUtils import getJsonFromFile
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
urlPath = "register"
registerJsonFile = "registerAPIValid.json"

# Testing Register API with body from file
def testRegisterApi():
    url = baseURI + urlPath
    payload = getJsonFromFile(registerJsonFile)
    response = postApiData(url, payload)
    print(response.json())
    assert response.status_code == 201



import random
import pytest
from utils.apiUtils import postApiData, daleteApiData
from utils.fileUtils import getJsonFromFile
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
regUrlPath = "register"
loginUrlPath = "login"
delUrlPath = "delete"
registerJsonFile = "registerAPIValid.json"
randNum = random.randint(0, 100)
eMail = "autoUser@test" + str(randNum)
paSsword = "1234"

@pytest.fixture()
def reg_user():
    payload = getPayloadDict_RegAPI(eMail, paSsword)
    regUrl = baseURI + regUrlPath
    reg_response = postApiData(regUrl, payload)
    assert reg_response.status_code == 201
    assert reg_response.json()["id"]
    data = reg_response.json()
    yield data ## Anything after this statement will run as a part of Teardown, or after the test function is executed.
    delUrl = baseURI + delUrlPath
    loginUrl = baseURI + loginUrlPath
    loginResponse = postApiData(loginUrl, payload)
    token = loginResponse.json()["token"]
    headers = {"x-access-token": token}
    payload = {"id": reg_response.json()["id"]}
    del_response = daleteApiData(delUrl, payload, headers)
    assert del_response.status_code == 200
    assert del_response.json()["id"] == reg_response.json()["id"]


def test_loginCorrectCreds(reg_user):
    payload = getPayloadDict_RegAPI(eMail, paSsword)
    url = baseURI + loginUrlPath
    resp = postApiData(url, payload)
    assert resp.status_code == 200

def test_loginEmptyPassword(reg_user):
    regUserData = reg_user
    payload = getPayloadDict_RegAPI(eMail, "")
    url = baseURI + loginUrlPath
    resp = postApiData(url, payload)
    assert resp.status_code == 401


def getPayloadDict_RegAPI(email=None, password=None):
    payload = getJsonFromFile(registerJsonFile)
    payload["email"] = email
    payload["password"] = password
    return payload

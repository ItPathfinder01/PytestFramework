import pytest
import requests

from utils.apiUtils import getApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
urlPath = "allusercount"


#Test API all users for status 200
def testAllUsersCountStatus200():
    url = baseURI + urlPath
    headers = {"accept": "application/json"}
    response = getApiData(url, headers)
    assert response.status_code == 200
    print(response.json())

# Test API all users for status 406
def testAllUsersCountStatus406():
    url = baseURI + urlPath
    response = getApiData(url)

    assert response.status_code == 406
    print(response.text)

def test_allUsersCountBody():
    url = baseURI + urlPath
    headers = {"accept": "application/json"}
    response = getApiData(url, headers)
    data = response.json()
    assert data["count"] == 4
    assert data["status"]["message"] == "success"
    assert data["status"]["status"] == 200


def test_getAllUsersCountTimeTaken():
    url = baseURI + urlPath
    headers = {"accept": "application/json"}
    response = getApiData(url, headers)
    data = response.json()
    print(response.elapsed.total_seconds())
    assert (response.elapsed.total_seconds()) <1
    print(data)

import pytest
from utils.fileUtils import getCsvDataAsDict, getDataAsTuple
from utils.apiUtils import postApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
dataFile = "registerAPIData.csv"
urlPath = "register"
dataFileWithStatus = "registerApiDataWithStatus.csv"
getData = getDataAsTuple(dataFileWithStatus)

# Data driven test from data file, inserting all data in single test

def test_dataDrivenRegAPI():
    url = baseURI + urlPath
    payloadList = getCsvDataAsDict(dataFile)
    for dataLines in payloadList:
        print((dataLines))
        response = postApiData(url, dataLines)
        assert response.status_code == 201
        data = response.json()
        print(data)
        assert data["id"]

# Datadriven from datafile, using Pytest parametrization, separate test for each raw in datafile
@pytest.mark.parametrize("input, respStatus", getData)
def test_dataDrivenParametrized(input, respStatus):
    url = baseURI + urlPath
    keys = ["email", "password"]
    requestDictionary = dict(zip(keys, input))
    print(("Request disctionary: ",requestDictionary, respStatus ))
    response = postApiData(url, requestDictionary)
    assert response.status_code == int(respStatus)



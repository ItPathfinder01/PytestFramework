from utils.myutils import *
from utils.myconfigparser import *

testURI = getPetAPIUrl()
petId = "120"

# Get by ID
def test_GetPetById_response():
    url = testURI + petId
    data, status, time = getAPIData(url)
    print("Server response:", data)
    assert int(data["id"]) == int(petId)
    assert status == 200
    print("Time taken ", time)

# Update API call
def test_updatingPet():
    payload = {"id": int(petId), "name": "Musia", "status": "wild"}
    data, status, time = putData(testURI, payload)
    assert data["id"] == int(petId)
    print(data)

#Delete API call
def test_deletePet():
    url = testURI + petId
    data, status, time = deleteData(url)
    assert data["message"] == petId
    assert data["code"] == 200
    print(data)

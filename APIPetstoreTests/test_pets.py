from utils.myutils import *
from utils.myconfigparser import *

# testURI = "https://petstore.swagger.io/v2/pet/"
testURI = getPetAPIUrl()
petId = "110"

def test_GetPetById_response():
    url = testURI + petId
    data, status, time = getAPIData(url)
    print("Server response:", data)
    assert int(data["id"]) == int(petId)
    assert status == 200
    print("Time taken ", time)

# Test updating a pet
def test_updatingPet():
    payload = {"id": int(petId), "name": "Musia", "status": "wild"}
    data, status, time = putData(testURI, payload)
    assert data["id"] == int(petId)
    print(data)


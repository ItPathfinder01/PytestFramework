from utils.myutils import getAPIData
from utils.myconfigparser import *

# testURI = "https://petstore.swagger.io/v2/pet/"
testURI = getPetAPIUrl()
petId = "120"

def test_GetPetById_response():
    url = testURI + petId
    data, status, time = getAPIData(url)
    print("Server response:", data)
    assert int(data["id"]) == int(petId)
    assert status == 200
    print("Time taken ", time)
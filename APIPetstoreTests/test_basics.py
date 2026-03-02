import requests, json

testURI = "https://petstore.swagger.io/v2/pet/"
petId = "20"

# test valid response or the response is not empty
def test_getPetById_response():
    url = testURI + petId
    header = {"content - type": "application / json"}
    response = requests.get(url, verify=False, headers=header)
    assert response.status_code == 200
    print("The status code is ", response.status_code)
    print("Requested URL ", url)
    data = response.json()
    print("The data is ", json.dumps(data, indent=3))
    assert len(data) > 0, "empty response"

# Testing response for  "id": 20
def test_getPetById_id():
    url = testURI + petId
    header = {"content - type": "application / json"}
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    assert int(data["id"]) == 20

# Test adding new pet to the store

def test_addPetToTheStore():
    url = testURI
    header = {"content - type": "application / json"}
    payload = dict(id=120, category={
        "id": 1,
        "name": "Domastik"
    }, name="Azazel", photoUrls=[
        "string"
    ], tags=[
        {
            "id": 10,
            "name": "Devil"
        }
    ], status="available")
    response = requests.post(url, verify=False, headers=header, json=payload)
    data = response.json()
    assert int(data["id"]) == 120
    assert len(data) > 0
    assert response.status_code == 200
    print(data)



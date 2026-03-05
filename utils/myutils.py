import requests, json

# Get API call and return response data
def getAPIData(url):
    headers = {"content - type": "application/json"}
    print("Request url ", url)
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    assert len(data) > 0, "Empty response"
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken


# Test updating a pet
def putData(url, body):
    headers = {"content - type": "application/json"}
    print("Request url ", url)
    print("Body ", json.dumps(body, indent=4))
    response = requests.put(url, verify=False, json=body, headers=headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, timeTaken, response.status_code


# Put API call
def deleteData(url):
    headers = {"content - type": "application/json"}
    print("Request url ", url)
    response = requests.delete(url, verify=False, headers=headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, timeTaken, response.status_code

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





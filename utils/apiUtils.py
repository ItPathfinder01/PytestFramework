import requests, json

def getApiData(url, opHeader=None):
    headers = {'Content-Type': 'application/json'}
    headers = (headers | opHeader) if isinstance(opHeader, dict) else headers
    response = requests.get(url, verify=False, headers=headers)
    print("\nRequestURL: " + url)
    print("request header:", response.request.headers)
    print("response header:", response.headers)
    return response

def postApiData(url, body):
    headers = {'Content-Type': 'application/json'}
    print("\n/ReqUrl:" + url)
    print("\n/ReqBody:" + json.dumps(body))
    return requests.post(url, verify=False, json=body, headers=headers)


import requests, json

def getApiData(url):
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, verify=False)
    return response
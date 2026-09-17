import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("API_KEY")

def get(path, params=None):
    r = requests.get(path, params=params, headers=headers)

    r.raise_for_status()

    if r.headers['content-type'] == 'application/json':
        return r.json()
    return r

baseUrl = 'http://www.tng-project.org/api/'
headers = {"api-key":api_key}

r = get(baseUrl)
name = "TNG50-1"
sim  = next((sim for sim in r['simulations'] if sim['name'] == name), None)



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
sim_obj  = next((sim for sim in r['simulations'] if sim['name'] == name), None)

sim = get(sim_obj['url'])

snapshots = get(sim['snapshots'])

z0snapshot = get(snapshots[-1]['url'])

subhalos = get(z0snapshot['subhalos'])


halo = get(subhalos['results'][80]['url']) #first halo




#mass history of this specific halo
m = [halo['mass']]
snaps = [halo['snap']]
for i in range(100):
    progenitor_url = halo['related']['sublink_progenitor']
    if progenitor_url:
        progenitor = get(progenitor_url)
    else:
        break

    print(progenitor)
    m.append(progenitor['mass'])
    snaps.append(progenitor['snap'])
    halo = progenitor

import matplotlib.pyplot as plt
plt.plot(snaps, m)
plt.xlabel("snap")
plt.ylabel("mass")
plt.grid()
plt.show()




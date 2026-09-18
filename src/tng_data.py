import requests
import h5py
from dotenv import load_dotenv
import os

def get(path, params=None):
    r = requests.get(path, params=params, headers=headers)

    r.raise_for_status()

    if r.headers['content-type'] == 'application/json':
        return r.json()

    if 'content-disposition' in r.headers:
        filename = r.headers['content-disposition'].split("filename=")[1]
        with open(filename, 'wb') as f:
            f.write(r.content)
        return filename

    return r

load_dotenv()
api_key = os.getenv("API_KEY")

baseUrl = 'http://www.tng-project.org/api/'
headers = {"api-key":api_key}


with h5py.File("mwm31s_satcatalog.hdf5", 'r') as f:
    sat_ids = f['SubfindIDSat'][:]
id = sat_ids[0] #first satelite z=0 id


url = "http://www.tng-project.org/api/TNG50-1/snapshots/99/subhalos/" + str(id) + "/"
halo = get(url)

cutout_request = {'dm':'Coordinates,Velocities'}
cutout = get(url+"cutout.hdf5", cutout_request)

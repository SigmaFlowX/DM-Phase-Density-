from tng_api_test import get

import h5py

with h5py.File("mwm31s_satcatalog.hdf5", 'r') as f:
    print(f.keys())
import h5py
import numpy as np
import pandas as pd


def cell_density(coords, vels, h, l):
    coords = np.asarray(coords) / h
    vels   = np.asarray(vels) / l
    idx = np.floor(np.hstack([coords, vels])).astype(np.int64)

    df = pd.DataFrame(idx, columns=['ix','iy','iz','ivx','ivy','ivz'])
    counts = df.groupby(list(df.columns)).size()
    density = counts / (h**3 * l**3)
    return 4.54e5 * density # *dm particle mass

def main():

    with h5py.File("cutout_342616.hdf5", 'r') as f:
        coordinates = f['PartType1']['Coordinates'][:]
        velocities = f['PartType1']['Velocities'][:]

    F = cell_density(coordinates, velocities, 10, 10)
    print(F.max())

if __name__ == "__main__":
    main()
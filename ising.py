'''
#Remove existing Numpy and/or Scipy:
!pip uninstall numpy scipy -y

#Install scipy built with Intel MKL:
!pip install intel-scipy
'''
import numpy as np
from array2gif import write_gif
import tensorflow
import pymc4 as pm


def to_two_color(lattice):
    blue = np.ones(lattice.shape, dtype=np.int) * 255 
    red = np.zeros(lattice.shape, dtype=np.int)
    red[lattice < 0] = 255 
    green = red 
    return np.array([red, green, blue])


def output_to_gif(dataset, filename, fps=8):
    print("Frames: {}".format(len(dataset)))
    colors = []
    write_gif(
        [to_two_color(lattice) for lattice in dataset],
        filename,
        fps=fps
    )

def get_dH(lattice, trial_location):
    """ H = - Sum_<ij>(s_i s_j) """
    i, j = trial_location
    height, width = lattice.shape
    H, Hflip = 0, 0
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ii = (i + di) % height
        jj = (j + dj) % width
        H -= lattice[ii, jj] * lattice[i, j]
        Hflip += lattice[ii, jj] * lattice[i, j]
    return Hflip - H


def get_H(spins):
    H = - (
        tt.roll(spins, 1, axis=1) * spins +
        tt.roll(spins, 1, axis=0) * spins +
        tt.roll(spins, -1, axis=1) * spins +
        tt.roll(spins, -1, axis=0) * spins
    )
    return H


def to_spins(lattice):
    return 2 * lattice - 1


def mc3_approach(T, width, height, N):
    shape = (height, width)
    x0 = np.random.randint(2, size=shape)
    with pm.model() as model:
        x = pm.Bernoulli('x', 0.5, shape=shape, testval=x0)
        magnetization = pm.Potential(
            'm',
            -get_H(to_spins(x)) / T
        )
        scaling = .0006
        mul = int(height * width * 1.75)
        step = pm.BinaryMetropolis([x], scaling=scaling)
        trace = pm.sample(N * mul * 5, step=step, chains=1, tune=False)
    dataset = [to_two_color(2 * t['x'] - 1) for t in trace[::mul * 5]]
    # Print out the final percent magnetization
    lattice = 2 * trace[-1]['x'] - 1
    print('Finished. Net magnetization: {:3.0%}'
              .format(abs(lattice.sum()) / lattice.size))
    return dataset


def run(width, height, N, T_over_Tc=.9):
    Tc = 2.269  # Normalized T := kT/J
    T = T_over_Tc * Tc
    dataset = None
    dataset = mc3_approach(T, width, height, N)
    filename = ('mc3_ising_{}_{}x{}.gif'
                   .format(T_over_Tc, width, height))


run(width=100, height=400, N=200)


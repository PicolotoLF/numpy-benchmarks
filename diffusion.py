#setup: import numpy as np;lx,ly=(2**7,2**7);u=np.zeros([lx,ly],dtype=np.double);u[lx/2,ly/2]=1000.0;tempU=np.zeros([lx,ly],dtype=np.double)
#run: diffusion(u,tempU,500)

#pythran export diffusion(float [][], float [][], int)
import numpy as np


def diffusion(u, tempU, iterNum):
    """
    Apply Numpy matrix for the Forward-Euler Approximation
    """
    mu = .1

    for n in range(iterNum):
        tempU[1:-1, 1:-1] = u[1:-1, 1:-1] + mu * (
            u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[0:-2, 1:-1] +
            u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, 0:-2])
        u[:, :] = tempU[:, :]
        tempU[:, :] = 0.0

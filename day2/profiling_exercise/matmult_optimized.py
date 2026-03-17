# Program to multiply two matrices using nested loops
import numpy as np
from line_profiler import profile

N = 250

@profile
def matrices(N):
    # NxN matrix
    X = np.matlib.rand(N, N)

    # Nx(N+1) matrix
    Y = np.matlib.rand(N, N + 1)

    # result is Nx(N+1)
    result = np.matmul(X, Y)

    print(result.shape)
    return result

matrices(N)

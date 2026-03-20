import numpy as np
import scipy
import matplotlib.pyplot as plt

## Linear algebra

### Define a matrix A

matrix_a = np.array([[1,-2,3],[4,5,6],[7,1,9]])

### Define a vector b

vector_b = np.array([1,2,3])

### Solve the linear system of equations A x = b

solution = scipy.linalg.solve(matrix_a, vector_b)
print(f"Solution x: {solution}")

### Check that your solution is correct by plugging it into the equation

verification = np.allclose(matrix_a @ solution, vector_b)
print(f"Is solution correct? {verification}")

### Repeat steps a-d using a random 3x3 matrix B (instead of the vector b)

matrix_b = np.random.random(9).reshape(3,3)
solution_b = scipy.linalg.solve(matrix_a, matrix_b)
print(f"Solution for second equation x: {solution}")

verification_b = np.allclose(matrix_a @ solution_b, matrix_b)
print(f"Is solution correct? {verification_b}")

### Solve the eigenvalue problem for the matrix A and print the eigenvalues and eigenvectors

eigenvalues, eigenvectors = scipy.linalg.eig(matrix_a)
print(f"Eigenvalues of matrix: {eigenvalues}.\n Eigenvector of matrix {eigenvectors}")

### Calculate the inverse, determinant of A

inv_determinant = scipy.linalg.det(scipy.linalg.inv(matrix_a))
print(f"The inverse determinant of matrix is: {inv_determinant}")

### Calculate the norm of A with different orders

frobenius_norm = scipy.linalg.norm(matrix_a, ord = 'fro')
nuclear_norm = scipy.linalg.norm(matrix_a, ord = 'nuc')
smallest_singular_value = scipy.linalg.norm(matrix_a, ord = -2)

print(f"Frobenius norm of matrix: {frobenius_norm}.\nNuclear norm of matrix {nuclear_norm}.\nSmallest singular value: {smallest_singular_value}")

## Statistics
### Create a discrete random variable with poissonian distribution and plot its probability mass function (PMF), cummulative distribution function (CDF) and a histogram of 1000 random realizations of the variable

X = scipy.stats.poisson(3.5)

n = np.arange(0,15)

fig, axes = plt.subplots(3,1, sharex=True)

axes[0].step(n, X.pmf(n))

axes[1].step(n, X.cdf(n))

axes[2].hist(X.rvs(size=1000))
plt.show()

## Create a continious random variable with normal distribution and plot its probability mass function (PMF), cummulative distribution function (CDF) and a histogram of 1000 random realizations of the variable

Y = scipy.stats.norm()

x = np.linspace(-5,5,100)

fig, axes = plt.subplots(3,1, sharex=True)

axes[0].plot(x, Y.pdf(x))

axes[1].plot(x, Y.cdf(x));

axes[2].hist(Y.rvs(size=1000), bins=50)
plt.show()

## Test if two sets of (independent) random data comes from the same distribution


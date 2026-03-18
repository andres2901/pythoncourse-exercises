import numpy as np

print(f"Create a null vector of size 10 but the fifth value which is 1")
null_vector = np.zeros(10)
null_vector[4] = 1
print(null_vector)

print(f"\nCreate a vector with values ranging from 10 to 49")
vector_range = np.arange(10, 50)
print(vector_range)

print(f"\nReverse a vector (first element becomes last)")
vector_range = np.flip(vector_range)
print(vector_range)

print(f"\nCreate a 3x3 matrix with values ranging from 0 to 8")
matrix  = np.arange(0,9).reshape(3,3)
print(matrix)

print(f"\nFind indices of non-zero elements from [1,2,0,0,4,0]")
search_array = np.array([1,2,0,0,4,0])
print(np.where(search_array != 0))

print(f"\nCreate a random vector of size 30 and find the mean value")
random_vector = np.random.random(30)
print(f"vector: {random_vector}. Mean: {np.mean(random_vector)}")

print(f"\nCreate a 2d array with 1 on the border and 0 inside")
new_array = np.array([[1,1,1],[1,0,1],[1,1,1]])
print(new_array)

print(f"\nCreate a 8x8 matrix and fill it with a checkerboard pattern")
checkboard = np.empty((8,8), dtype = np.int32)
checkboard[0::2] = np.array([1,0,1,0,1,0,1,0])
checkboard[1::2] = np.array([0,1,0,1,0,1,0,1])
print(checkboard)

print(f"\nCreate a checkerboard 8x8 matrix using the tile function")
line_one = np.tile([1,0],4)
line_two = np.tile([0,1],4)
checkboard = np.tile([line_one,line_two],(4,1))
print(checkboard)

print(f"\nGiven a 1D array, negate all elements which are between 3 and 8, in place")
Z = np.arange(11)
Z[(Z > 3) & (Z < 8)] *= -1
print(Z)

print(f"\nCreate a random vector of size 10 and sort it")
Z = np.random.random(10)
Z = np.sort(Z)
print(Z)

print(f"\nConsider two random array A anb B, check if they are equal")
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = (A==B).all()
print(equal)

print(f"\nHow to calculate the square of every number in an array in place (without creating temporaries)?")
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = np.square(Z)
print(Z.dtype)
print(Z)

print(f"\nHow to get the diagonal of a dot product?")
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diagonal(C)
print(D)

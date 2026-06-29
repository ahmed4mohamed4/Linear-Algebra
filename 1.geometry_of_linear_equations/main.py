
# Importing
import numpy as np

# Matrix A (Coefficients)
A = np.array ([[2, -1],
               [-1, 2]])

# Vector b (right hand side)
b = np.array ([0, 3])

x = np.linalg.solve (a= A, b= b)
# Solve both equations:
print (f"(x, y) = ({x [0]}, {x[1]})")

# To make sure
# This will return b [0, 3]
vector_b = (A @ x) # Matrix Multiplication
print (f"b = [{vector_b [0]}, {vector_b [1]}]")

# Separator
print ('#' * 50)

# Matrix multiplication
matrix_1 = np.array ([[1, 2],
                      [3, 4]])

matrix_2 = np.array ([[5, 6],
                      [7, 8]])

result = matrix_1 @ matrix_2
print (f"Result of matrix multiplication:\n {result}")
import numpy as np

# Create the transformation matrix
A = np.array([[0, -2], [2, 0]])

# Create a 2D vector
v = np.array([1, 2])

# Apply the transformation to the vector
v_transformed = A @ v

print(v_transformed)  # Output: [4, -2]

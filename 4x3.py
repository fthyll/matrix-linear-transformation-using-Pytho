import numpy as np

# Create the transformation matrix
A = np.array([[1, 0, 0],
              [0, 2, 0],
              [0, 0, 3],
              [0, 0, 0]])

# Create a 3D vector
v = np.array([1, 2, 3])

# Apply the transformation to the vector
v_transformed = A @ v

print(v_transformed)  # Output: [1, 4, 9, 0]

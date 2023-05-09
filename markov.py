# import packages
import numpy as np

# Create Initial State Matrix
initial_state = np.array([0.22, 0.20, 0.19, 0.18, 0.16, 0.04, 0.01])

# Create Identity Matrix
i_matrix = np.identity(7)

# Create Transition Matrix
t_matrix = np.array([
    [0, 0.619, 0, 0, 0, 0, 0, 0.381],
    [0, 0, 0.579, 0, 0, 0, 0, 0.421],
    [0, 0, 0, 0.591, 0, 0, 0, 0.409],
    [0, 0, 0, 0, 0.498, 0, 0, 0.502],
    [0, 0, 0, 0, 0, 0.06, 0.00187, 0.93813],
    [0, 0, 0, 0, 0, 0, 0.03467, 0.96533],
    [0, 0, 0, 0, 0, 0, 0.22, 0.78],
    [0, 0, 0, 0, 0, 0, 0, 1]
])

# Create Q Matrix
q_matrix = t_matrix[:-1, :-1]

# Absorption probability matrix
r_matrix = np.array([
    [0.381],
    [0.421],
    [0.409],
    [0.502],
    [0.93813],
    [0.96533],
    [0.78],
])

# 1 Matrix
c_matrix = np.array([
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
])

# N Matrix
n = np.linalg.inv((i_matrix - q_matrix))
# n = n.round(2)


# Time to absorption Matrix
t = np.matmul(n, c_matrix)


# Absorption Probability Matrix
b = np.matmul(n, r_matrix)
print("probablity absorption")
print(b)

# %% [markdown]

# Efficient Python The Numpy Power

# Numpy

# What is numpy?
# Numpy is a fundamental python library to numeriral operation for data. As know as mumpy is usually more fast than built in python functios.
# Numpy is really more fast than pyhon functions, because it is homogenous, i.e all elements has the same type. All element are arrays in numpy and each
# arry must have just one type.
# %%
# How can is create a numpy object?
import numpy as np

# No numpy elements
numbers = list(range(5))
print("No numpy list:", numbers)

number_numpy = np.array(range(5))
print("Numpy array:", number_numpy)

# %% [markdown]

# NumPy uses broadcast mythologies to do operations quickly. When we need a multiplicative operation on the vector with a scalar, NumPy uses the broadcasting procedure. With this, we do not need to make loops or use list comprehension to perform math operations on vectors or matrices.

# %%
numbers = np.array([1, 2, 3, 4])
print("Multiple by 10:", numbers * 10)
print("Power of 2:", numbers ** 2)

# %% [markdown]
# Numpy Indexing

# How to get an element in a 1 or 2D array?
# %%
# A matrix or a 2-d array in numpy
matrix = np.array([
    [4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5]
])
print("Numpy 2d array:", matrix)

# Get first row and second row
print("First row", matrix[0, ])
print("First row", matrix[0, :])
print("First row", matrix[0, :2])
print("First row", matrix[0, :-2])
print("Second row", matrix[1, ])
print("Second row", matrix[1, 1:3])

# Show all elements with values more than 4
print("n > 4:", matrix[matrix > 4])

# Math Operations
print("Math: ", matrix * 2)

# Replace values
# get the 3th elemnt for each row and replace with ten
matrix[:, 2] = 10
print("Repalced matrix: ", matrix)

# Workin with Boolean indexing

print("Boolean conditions: ", matrix > 9)
print("Boolean indexing: ", matrix[matrix > 9])

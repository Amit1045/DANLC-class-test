#python programs...
#Q1
# Create arrays of 10 zeros, 10 ones, and 10 fives
import numpy as np


zeros_array = np.zeros(10)
ones_array = np.ones(10)
fives_array = np.full(10, 5)

# Print the output
print("Array of 10 zeros:", zeros_array)
print("Array of 10 ones:", ones_array)
print("Array of 10 fives:", fives_array)

# Q2
# Create a 3x3 matrix with values ranging from 2 to 10
matrix = np.arange(2, 11).reshape(3, 3)

# Print the output
print("3x3 Matrix with values ranging from 2 to 10:")
print(matrix)

#Q3
# Create an array with values ranging from 12 to 38
array = np.arange(12, 39)  # 39 is exclusive

# Print the output
print("Array with values ranging from 12 to 38:")
print(array)

#Q4
# Input list and tuple
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_tuple = ([8, 4, 6], [1, 2, 3])

# Convert list and tuple into arrays
array_from_list = np.array(my_list)
array_from_tuple = np.array(my_tuple)

# Print the output
print("Array from list:", array_from_list)
print("Array from tuple:", array_from_tuple)

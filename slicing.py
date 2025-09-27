import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])


#base slicing
print(arr[2:7])
# Output: [2 3 4 5 6]

#step slicing
print(arr[1:8:2])
# Output: [1 3 5 7]

#take off start and stop
print(arr[::3])
# Output: [0 3 6]


#use negative indices
print(arr[-5:])
# Output: [5 6 7 8 9]

print(arr[:-5])
# Output: [0 1 2 3 4]
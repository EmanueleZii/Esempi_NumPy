import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#indexing 
print(arr[0, 0]) # Output: 1

#slicing
print(arr[0:2, 1:3])
# Output: [[2 3] [5 6]]

#boolenan indexing
print(arr[arr > 5]) # Output: [6 7 8 9]


arr_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

#slicing on rows
print(arr_2d[1, 2]) # Output: [[ 5 6 7 8]
                    # [ 9 10 11 12]]

#slicing on columns
print(arr_2d[:, 1]) # Output: [20 50 80]

#slicing mixed
print(arr_2d[0:2, 1:3]) # Output: [[20 30] [50 60]]
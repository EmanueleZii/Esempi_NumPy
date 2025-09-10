import numpy as np

# Creazione di un array con un tipo di dato specifico
arr = np.array([1, 2, 3],   dtype='int32')
print(arr.dtype) # Output: int32

# Creazione di un array bidimensionale
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape) # Output: (2, 3)

#  Arange 
arr = np.arange(10)
print(arr) # Output: [0 1 2 3 4 5 6 7 8 9]

arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)
# Output: [[0 1 2] [3 4 5]]
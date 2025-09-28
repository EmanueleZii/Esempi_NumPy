import numpy as np

arr = np.array([10, 20, 30, 40, 50])

#facing
indices = np.array([1, 3])
print(arr[indices]) # Output: [20 40]

indices_2d = [0,2,4]
print(arr[indices_2d]) # Output: [10 30 50]


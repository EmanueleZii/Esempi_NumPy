import numpy as np


arr = np.array([1, 2, 3, 4])

scalar = 10

result = arr + scalar
print(result)  # Output: [11 12 13 14]


a = np.array([1, 2, 3])
b = np.array([4,5,6])
result = a + b
print(result)  # Output: [5 7 9]

d = np.sin(a)
print(d)  # Output: [0.84147098 0.90929743 0.14112001]

e = np.dot(a, b)
print(e)  # Output: 32

f = a+b
print(f)  # Output: [5 7 9]
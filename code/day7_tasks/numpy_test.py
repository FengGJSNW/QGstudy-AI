import numpy as np

a = np.array([
    [i for i in range(0,3)],
    [i for i in range(3,6)],
    [i for i in range(6,9)],
    [i for i in range(9,12)]
])

b = np.array([np.arange(i, i+4) for i in range(0, 11, 4)])

print(a)
print(b)

print(a.shape)
print(a.dtype)
print(a.ndim)

b = b.T
print(b)

flat = b.reshape(-1)
print(flat)
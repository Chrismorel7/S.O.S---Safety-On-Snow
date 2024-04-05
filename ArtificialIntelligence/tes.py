import numpy as np


w2array = np.loadtxt("w2.txt").reshape(-1, 1)

w1array = np.loadtxt("w1.txt")

print("NumPy array:")
print("\n\n",w1array)
print("\n\n",w2array)


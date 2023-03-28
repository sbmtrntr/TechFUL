import numpy as np

n = int(input())
data = np.array([[int(x) for x in input().split()] for _ in range(n)])

label = data[:, 0]

print(label)
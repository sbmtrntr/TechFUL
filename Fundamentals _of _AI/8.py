import numpy as np
A = list(map(int, input().split()))
D = list(map(int, input().split()))

A = np.array(A)
print(A.reshape(D))
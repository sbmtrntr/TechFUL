import numpy as np 

data = list(map(int, input().split()))
data = np.array(data)
N = len(data)
print(data[3:N-3])
print(data[:N:2])
print(data[::-1])
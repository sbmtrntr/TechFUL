import numpy as np
N = int(input())
x = np.array([])
for _ in range(N):
    x = np.append(x, int(input()))

avg = np.mean(x)
std = np.std(x)

ans = np.round((x[0] - avg) / std, decimals = 3)
print(ans)
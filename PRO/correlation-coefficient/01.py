import numpy as np

N = int(input())

X = [[0.0]*N for i in range(5)]

for i in range(5):
    X[i] = [float(x) for x in input().split()]

Y = [float(x) for x in input().split()]

for i in range(5):
    ans = str(round(np.corrcoef(X[i], Y)[0][1], 2))
    if len(ans) >= 4:
        print(ans)
    else:
        print(ans + '0')
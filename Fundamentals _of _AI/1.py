N = int(input())
X = [int(x) for x in input().split()]
X.sort()
MAX = X[-1]
MIN = X[0]
if N % 2 == 0:
    MEDIAN = (X[(N-1)//2] + X[N//2]) / 2
else:
    MEDIAN = X[N//2]

print(MAX)
print(MIN)
print(MEDIAN)
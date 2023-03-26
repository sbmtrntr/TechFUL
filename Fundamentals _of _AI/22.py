import math

N = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

X_mean = sum(X) / N
Y_mean = sum(Y) / N

cov_XY = sum([(X[i] - X_mean)*(Y[i] - Y_mean) for i in range(N)]) / N
X_sigma = math.sqrt(sum([(X[i] - X_mean)**2 for i in range(N)]) / N)
Y_sigma = math.sqrt(sum([(Y[i] - Y_mean)**2 for i in range(N)]) / N)

r_XY = cov_XY/(X_sigma*Y_sigma)

print(round(r_XY,2))
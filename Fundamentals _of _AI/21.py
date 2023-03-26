N = int(input())
X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]

# 共分散を求める際に必要なXとYの平均値を計算してください。
X_mean = sum(X) / N
Y_mean = sum(Y) / N

# XとYの共分散を計算してください。
cov_XY = sum([(X[i] - X_mean) * (Y[i] - Y_mean) for i in range(N)]) / N

# 小数点第3位を四捨五入して出力
print(round(cov_XY,2))
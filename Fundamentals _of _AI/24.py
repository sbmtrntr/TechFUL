import numpy as np

n = int(input())
x, y = np.array([0]*n), np.array([0]*n)
for i in range(n):
    x[i], y[i] = map(int, input().split())
x_t1 = int(input())
x_t2 = int(input())

# 係数の計算
a = sum([(x[i] - np.mean(x))*(y[i] - np.mean(y)) for i in range(n)]) / n / np.var(x)
b = np.mean(y) - a*np.mean(x)

# 計算した係数を用いて値を計算
y_t1 = a*x_t1 + b
y_t2 = a*x_t2 + b

# 小数第1位を四捨五入して出力
print(round(y_t1))
print(round(y_t2))
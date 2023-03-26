import numpy as np

n = int(input())
x, y = np.array([0]*n), np.array([0]*n)
for i in range(n):
    x[i], y[i] = map(int, input().split())
x_t1 = int(input())
x_t2 = int(input())

#係数の計算
X = np.matrix([[1, x[i], x[i]**2] for i in range(n)])
Y = np.matrix(np.matrix(y).T)

w = (X.T*X)**-1*X.T*Y

#結果の出力
y_t1 = w.T*(np.matrix([1, x_t1, x_t1**2]).T)
y_t2 = w.T*(np.matrix([1, x_t2, x_t2**2]).T)

y_t1 = np.float(y_t1[0][0])
y_t2 = np.float(y_t2[0][0])

print(round(y_t1))
print(round(y_t2))
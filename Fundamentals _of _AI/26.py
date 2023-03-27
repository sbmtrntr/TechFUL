import numpy as np

alpha = 0.01

N,M = map(int, input().split())

w = np.array([float(x) for x in input().split()])
train = np.array([[float(x) for x in input().split()] for _ in range(N)])
t = np.array([[float(x) for x in input().split()] for _ in range(M)])
x = train[0:N,0:2]
l = train[0:N,2:3].astype(np.int)
flag = True
### 以下にコードを入力してください。
while flag:
    flag = False
    for i in range(N):
        y = -1.0*w[0] + x[i][0]*w[1] + x[i][1]*w[2]
        if y > 0:
            e = l[i] - 1
        else:
            e = l[i] - 0

        w[0] += -alpha*e
        w[1] += alpha*e*x[i][0]
        w[2] += alpha*e*x[i][1]

        if e != 0:
            flag = True

for i in range(M):
    y = -1.0*w[0] + t[i][0]*w[1] + t[i][1]*w[2]
    if y > 0:
        print(1)
    else:
        print(0)
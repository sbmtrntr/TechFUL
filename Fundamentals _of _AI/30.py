import numpy as np 
n,p,m = map(int, input().split())

v = np.array([[float(x) for x in input().split()] for _ in range(n)])
a = np.array([float(x) for x in input().split()])
w = np.array([[float(x) for x in input().split()] for _ in range(p)])
b = np.array([float(x) for x in input().split()])
x = np.array([float(x) for x in input().split()])

### ステップ関数
def step_func(x):
    y = np.where(x>0, 1.0, 0.0)
    return y

### 以下にコードを入力してください。
temp = v.T * x
h = step_func(temp.sum(axis=1) + a)
temp = w.T * h
y = step_func(temp.sum(axis=1) + b)
### ここまで
print(y)                            
import numpy as np 
n,p,m = map(int, input().split())

v = np.array([[float(x) for x in input().split()] for _ in range(n)])
a = np.array([float(x) for x in input().split()])
w = np.array([[float(x) for x in input().split()] for _ in range(p)])
b = np.array([float(x) for x in input().split()])
x = np.array([float(x) for x in input().split()])

### 以下にコードを入力してください。(ヒント： ハイパボリックタンジェント関数は np.tanh() を用いて計算することができます。)
temp = v.T * x
h = np.tanh(temp.sum(axis=1) + a)
temp = w.T * h
y = np.tanh(temp.sum(axis=1) + b)
### ここまで
print(y)
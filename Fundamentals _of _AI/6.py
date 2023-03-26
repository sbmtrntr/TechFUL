import numpy as np 

seed = int(input())
np.random.seed(seed)

A = np.random.rand(3,3)
B = np.random.rand(3,3)

### ここから
# ヒント：NumPyを用いて計算をおこなってください。

# 行列積を計算してください。
x = np.dot(A, B)

# アダマール積を計算してください。
y = np.multiply(A, B)

### ここまで

print(x)
print(y)
import numpy as np

n = int(input())
x = np.array([float(x) for x in input().split()])
w = np.array([float(x) for x in input().split()])
h = float(input())

### 以下にコードを入力してください。
u = sum(x * w)
if u > h:
    print(1)
else:
    print(0)
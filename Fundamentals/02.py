import numpy as np

n = int(input())
x = list(map(int, input().split()))
x = np.array(x)

### ここから

# arr平均の計算
avg = np.mean(x)

### ここまで

# int型にキャストして、小数点以下切り捨て
avg = int(avg)

# 出力
print(avg)

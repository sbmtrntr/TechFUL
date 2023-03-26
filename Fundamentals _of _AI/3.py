import numpy as np

n = int(input())
x = list(map(int, input().split()))
x = np.array(x)

### ここから

# 分散の計算
var = np.var(x)

# 標準偏差の計算
# varの値を用いる場合は、小数点以下切り捨てをせずに用いてください。
std = np.std(x)

### ここまで

# int型にキャストして、小数点以下切り捨て
var = int(var)
std = int(std)

# 出力
print(var)
print(std)
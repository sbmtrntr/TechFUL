import numpy as np 

# 標準入力から配列を得る
data = list(map(int, input().split()))
data = np.array(data)

### ここから

# 条件を穴埋めしてください
indexes = np.where(data % 2 == 0)

### ここまで

# インデックスを出力
print(indexes[0])

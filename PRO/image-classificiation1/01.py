import numpy as np

n = int(input())
m = int(input())
data = list(map(int, input().split()))
data = np.array(data)
data = data.reshape([n, m, 3])

#変換後のdataをのshapeを出力してください
print(data.shape)
import numpy as np


def print_values(mov_avg, mov_var):

    def print_value(value):
        value = [f"{v:.2f}" for v in value]
        value = " ".join(value)
        print(value)

    print_value(mov_avg)
    print_value(mov_var)


n = int(input())
x = list(map(int, input().split()))
x = np.array(x)
k = int(input())

### ここから
# 移動平均を計算
mov_avg = [0]*n
for i in range(n):
    if i < k-1:
        mov_avg[i] = np.mean(x[:i+1])
    else:
        mov_avg[i] = np.mean(x[i-k+1:i+1])



# 移動分散を計算
mov_var= [0]*n
for i in range(n):
    if i < k-1:
        mov_var[i] = np.var(x[:i+1])
    else:
        mov_var[i] = np.var(x[i-k+1:i+1])
### ここまで

# 出力
print_values(mov_avg, mov_var)
import numpy as np

N, seed = map(int, input().split())

# seedを設定してから、xをサンプリング。この部分は書き換えないでください。
np.random.seed(seed)
x = np.random.uniform(-1, 1, N)

def step_func(x):
    ### 以下にコードを入力してください。(ヒント： np.where)
    y = np.where(x >= 0, 1, 0)
    ### ここまで

    # np.int型にキャストして出力
    return y.astype(np.int)

y = step_func(x)
sum_y = np.sum(y)

print(y, sum_y)
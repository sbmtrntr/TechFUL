import numpy as np


# n　入力数　p 中間数 m 出力数
n, p, m, N = map(int, input().split())
# v 隠れ層の重み
v = np.array([[float(x) for x in input().split()] for _ in range(n)])
# a 隠れ層のバイアス
a = np.array([float(x) for x in input().split()])
# w 出力層の重み
w = np.array([[float(x) for x in input().split()] for _ in range(p)])
# b 出力層のバイアス
b = np.array([float(x) for x in input().split()])
# x 入力
x = np.array([[float(x) for x in input().split()] for _ in range(N)])
# t 教師信号
t = np.array([[float(x) for x in input().split()] for _ in range(N)])


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def forward(x):
    h = sigmoid(x @ v + a)
    y = h @ w + b
    return y, h


def backward(x, h, y, t):
    # 勾配計算：w, b
    delta2 = y - t
    # 行列積を用いることで、各データから求められるwの勾配の和が得られます。
    # 更新の際は平均を使うので、勾配の和をデータの数で割ります。
    grad_w = h.T @ delta2 / N
    grad_b = np.sum(delta2, axis=0) / N

    # 勾配計算：v, a
    sigmoid_dash = h * (1-h)
    delta1 = (delta2 @ w.T) * sigmoid_dash
    grad_v = x.T @ delta1 / N
    grad_a = np.sum(delta1, axis=0) / N

    return grad_v, grad_a, grad_w, grad_b


# 学習率の設定
lr = 0.1

# 誤差逆伝播を用いて勾配を計算
y, h = forward(x)
grad_v, grad_a, grad_w, grad_b = backward(x, h, y, t)

# 勾配に基づいて重みとバイアスを更新
v -= lr * grad_v
a -= lr * grad_a
w -= lr * grad_w
b -= lr * grad_b

# 更新した重みとバイアスを使って予測し、出力
y, _ = forward(x)
print(y)
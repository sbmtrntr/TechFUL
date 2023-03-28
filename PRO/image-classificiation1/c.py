import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

INPUT_NUM = 100  # 入力の数：100次元
OUTPUT_NUM = 2  # 出力の数：分類の数
HIDDEN_NUM = 64 # 中間層の数 : 任意に変更可能

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 層を定義　Linearは全結合層
        self.fc1 = nn.Linear(INPUT_NUM, HIDDEN_NUM)
        self.fc2 = nn.Linear(HIDDEN_NUM, OUTPUT_NUM)

    def forward(self, input):
        # フォワードを定義
        x = F.relu(self.fc1(input)) # 活性化関数はReLU
        x = F.softmax(self.fc2(x),dim=0) # 活性化関数はsoftmax
        return x

model = Net()

seed = 0
np.random.seed(seed)
torch.manual_seed(seed)

# modelのパラメータを辞書型で取得して確認してみましょう
params = model.state_dict()
print(params)
# 入力100，中間層64なので，fc1の重みは，64×100の配列になっているはずです．
print(params["fc1.weight"])

test_input = torch.from_numpy(np.random.rand(100).astype(np.float32))
y = model(test_input)
print(y.data)
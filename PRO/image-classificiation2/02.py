import torch
import torch.nn as nn

class Pool(nn.Module):
    def __init__(self):
        super().__init__()
        ### 各プーリングを定義してください。
        self.max_pool = nn.MaxPool2d(2) # 最大プーリングを定義する
        self.avg_pool = nn.AvgPool2d(2) # 平均プーリングを定義する
        ### ここまで

    def forward(self, x):
        x = self.max_pool(x)
        x = self.avg_pool(x)
        return x 


# シード値の設定
seed = int(input())
torch.manual_seed(seed)

# データの生成
x = torch.rand(1, 1, 8, 8, dtype=torch.float)

# モデルの生成
model = Pool()

# 結果の出力
y = model(x)
print(y.data)

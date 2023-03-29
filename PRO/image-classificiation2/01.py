import torch 
import torch.nn as nn 
import torch.nn.functional as F

# モデルの定義
class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        ### 畳み込み層を定義してください。
        self.conv1 = nn.Conv2d(3, 4, 5, padding=2)
        self.conv2 = nn.Conv2d(4, 2, 3)
        ### ここまで

    def forward(self, x):
        ### 順伝播の計算するコードを入力してください。
        x = F.relu(self.conv1(x))
        x = self.conv2(x)
        ### ここまで

        # 全結合層に入力できるように形を整える
        x = torch.flatten(x)
        return x

# シード値の設定
seed = int(input())
torch.manual_seed(seed)

# データの生成
x = torch.rand(1, 3, 7, 7, dtype=torch.float)

# モデルの生成
model = CNN()

# 結果の出力
y = model(x)
print(y.data)
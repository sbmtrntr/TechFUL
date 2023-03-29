import torch
import torch.nn as nn
import torch.nn.functional as F
in_channels=3
out_channels=16
kernel_size=3
padding=1
conv = nn.Conv2d(in_channels, out_channels, kernel_size, padding=padding)

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3 , 32, 7, padding=3)
        self.conv2 = nn.Conv2d(32, 64, 5, padding=2)
        # 全結合層の入力は、self.conv2が出力した特徴マップのサイズ。
        self.fc1 = nn.Linear(64*32*32, 128)
        self.fc2 = nn.Linear(128, 2)
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        # Linearに入力するために形を整える
        x = torch.flatten(x)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = CNN()
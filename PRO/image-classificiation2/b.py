import torch.nn as nn 
import torch.nn.functional as F

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3 , 32, 7, padding=3)
        self.conv2 = nn.Conv2d(32, 64, 7, padding=3)
        self.avg_pool = nn.AvgPool2d(2)
        self.max_pool = nn.MaxPool2d(2)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.avg_pool(x) # 平均プーリング
        x = F.relu(self.conv2(x))
        x = self.max_pool(x) # 最大プーリング
        return x
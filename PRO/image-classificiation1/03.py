import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

#seed値の設定
seed = int(input())
np.random.seed(seed)
torch.manual_seed(seed) 

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        #層を定義してください
        self.fc1 = nn.Linear(100, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 2)

    def forward(self, input):
        # forwardを定義してください
        x = F.relu(self.fc1(input)) # 活性化関数はReLU
        x = F.relu(self.fc2(x)) # 活性化関数はReLU
        x = F.softmax(self.fc3(x),dim=0) # 活性化関数はsoftmax
        return x

model = Net()

x = torch.from_numpy(np.random.rand(100).astype(np.float32))
y = model(x)
print(y.data)
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import torch.optim as optim

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
        x = F.relu(self.fc1(input))
        x = F.relu(self.fc2(x))
        x = F.log_softmax(self.fc3(x),dim=1)
        return x

model = Net()

#train_data : 200個（それぞれのラベルにつき100個ずつ）
#test_data : 10個
train_data1 = np.random.randint(0,128,(100,100))
train_data2 = np.random.randint(128,256,(100,100))
train_data = np.concatenate([train_data1,train_data2])
train_label = np.concatenate([np.zeros(100),np.ones(100)])

test_data = np.random.randint(0,256,(10,100))

# 正規化
train_data = train_data/255
test_data = test_data/255

train_data = torch.from_numpy(train_data).float()
train_label = torch.from_numpy(train_label).long()
test_data = torch.from_numpy(test_data).float()

#誤差関数:NLLLossを使用
criterion = F.nll_loss

# optimizer:SGDを使用
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

for epoch in range(1):
    #学習部分のコードを書いてください
    optimizer.zero_grad() 
    outputs = model(train_data)
    loss = criterion(outputs, train_label)
    loss.backward()
    optimizer.step()

with torch.no_grad():
    outputs = model(test_data)
    _, predicted = torch.max(outputs.data, 1)
    print(predicted.data.numpy())
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import torch.optim as optim

#再現性を保つためにseedを固定
seed = 0
np.random.seed(seed)
torch.manual_seed(seed) 

class CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 64, 5, padding=2)
        self.conv2 = nn.Conv2d(64, 128, 3, padding=1)
        self.fc1 = nn.Linear(128*8*8, 128)
        self.fc2 = nn.Linear(128, 2)
        self.max_pool = nn.MaxPool2d(2)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.max_pool(x)
        x = F.relu(self.conv2(x))
        x = self.max_pool(x)
        # print(x.shape)
        x = x.view(x.size()[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.log_softmax(x, dim=1)
        return x

model = CNN()

device = torch.device("cuda")

#誤差関数 : nll_lossを使用
criterion = F.nll_loss

# optimizer : SGDを使用
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

#train_data : 140個 (チンパンジーとサルが70個ずつ)
#validation_data : 111個
train_data = np.loadtxt('train.csv', delimiter=',', dtype='uint8', skiprows=1)[:,1:]
train_label = np.loadtxt('train.csv', delimiter=',', dtype='uint8', skiprows=1,usecols=[0])
validation_data = np.loadtxt('test.csv', delimiter=',', dtype='uint8', skiprows=1)[:,1:]

train_data = train_data.reshape([140, 3, 32, 32])
validation_data = validation_data.reshape([111, 3, 32, 32])

# 正規化
validation_data = validation_data / 255
train_data = train_data / 255

train_data = torch.from_numpy(train_data).float()
train_label = torch.from_numpy(train_label).long()
validation_data = torch.from_numpy(validation_data).float()

for epoch in range(3000):
    #データ全ての合計のロス
    running_loss = 0.0
    # optimizerの初期化
    optimizer.zero_grad()
    outputs = model(train_data)
    loss = criterion(outputs, train_label)
    loss.backward()
    optimizer.step()
    running_loss += loss.item()
    if epoch % 50 == 0:
        print(epoch, running_loss)

# 検証データの推論
with torch.no_grad():
    outputs = model(validation_data)
    _, predicted = torch.max(outputs.data, 1)

predicted = predicted.tolist()

print(predicted)

f = open("submission.csv", 'w')
f.write('id, label\n')
for i in range(1, 112):
    f.write(str(i) + ', ' + str(predicted[i-1]) + '\n')
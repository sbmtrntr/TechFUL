import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import torch.optim as optim

INPUT_NUM = 3072  # 入力の数
OUTPUT_NUM = 2  # 出力の数
HIDDEN_NUM = 256 # 中間層の数

#再現性を保つためにseedを固定
seed = 0
np.random.seed(seed)  
torch.manual_seed(seed) 

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(INPUT_NUM, HIDDEN_NUM)
        self.fc2 = nn.Linear(HIDDEN_NUM, HIDDEN_NUM)
        self.fc3 = nn.Linear(HIDDEN_NUM, OUTPUT_NUM)

    def forward(self, input):
        x = F.relu(self.fc1(input))
        x = F.relu(self.fc2(x))
        x = F.log_softmax(x, dim=1)
        return x

model = Net()

#誤差関数 : NLLLossを使用
criterion = F.nll_loss

# optimizer : SGDを使用
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

#train_data : 60個 (チンパンジーとサルが30個ずつ)
#validation_data : 135個
train_data = np.loadtxt('train.csv', delimiter=',', dtype='uint8', skiprows=1)[:,1:]
train_label = np.loadtxt('train.csv', delimiter=',', dtype='uint8', skiprows=1,usecols=[0])
validation_data = np.loadtxt('test.csv', delimiter=',', dtype='uint8', skiprows=1)[:,1:]

# 正規化
validation_data = validation_data / 255
train_data = train_data / 255

train_data = torch.from_numpy(train_data).float()
train_label = torch.from_numpy(train_label).long()
validation_data = torch.from_numpy(validation_data).float()

for epoch in range(500):
    #データ全ての合計のロス
    running_loss = 0.0
    # optimizerの初期化
    optimizer.zero_grad()
    outputs = model(train_data)
    loss = criterion(outputs, train_label)
    loss.backward()
    optimizer.step()
    running_loss += loss.item()

# 検証データの推論
with torch.no_grad():
    outputs = model(validation_data)
    _, predicted = torch.max(outputs.data, 1)

predicted = predicted.tolist()

f = open("submission.csv", 'w')
f.write('id, label\n')
for i in range(1, 136):
    f.write(str(i) + ', ' + str(predicted[i-1]) + '\n')
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import torch.optim as optim

INPUT_NUM = 100  # 入力の数：100
OUTPUT_NUM = 2  # 出力の数：分類の数
HIDDEN_NUM = 64 # 中間層の数 : 任意に変更可能

#再現性を保つためにseedを固定
seed = 0
np.random.seed(seed)  
torch.manual_seed(seed) 

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(INPUT_NUM, HIDDEN_NUM)
        self.fc2 = nn.Linear(HIDDEN_NUM, OUTPUT_NUM)

    def forward(self, input):
        x = F.relu(self.fc1(input))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

model = Net()

#誤差関数 : NLLLossを使用
criterion = F.nll_loss

# optimizer : SGDを使用
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

#train_data : 200個（それぞれのラベルにつき100個ずつ）
#validation_data : 20個（それぞれのラベルにつき10個ずつ）

train_data1 = np.random.randint(0,128,(100,100))
train_data2 = np.random.randint(128,256,(100,100))
train_data = np.concatenate([train_data1,train_data2])
train_label = np.concatenate([np.zeros(100),np.ones(100)])

validation_data1 = np.random.randint(0,128,(10,100))
validation_data2 = np.random.randint(128,256,(10,100))
validation_data = np.concatenate([validation_data1,validation_data2])
validation_label = np.concatenate([np.zeros(10),np.ones(10)])

# 正規化
validation_data = validation_data/255
train_data = train_data/255

train_data = torch.from_numpy(train_data).float()
train_label = torch.from_numpy(train_label).long()
validation_data = torch.from_numpy(validation_data).float()
validation_label = torch.from_numpy(validation_label).long()

for epoch in range(304):
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
        correct = (predicted == validation_label).sum().item()
        accuracy = correct/len(validation_data)
    print('epoch : %d loss: %.3f accuracy: %.1f' % (epoch + 1, running_loss / len(train_data), accuracy))
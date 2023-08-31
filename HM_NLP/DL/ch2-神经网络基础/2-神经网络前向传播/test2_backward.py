import torch
import torch.nn as nn
import torch.optim as optim

# 创建模型
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(2, 1)

    def forward(self, x):
        return self.linear(x)

# 创建模型和损失函数
model = SimpleModel()
criterion = nn.MSELoss()

# 创建优化器
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 输入数据
inputs = torch.tensor([[1.0, 2.0]])
targets = torch.tensor([[0.0]])

# 前向传播
outputs = model(inputs)

# 计算损失
loss = criterion(outputs, targets)

# 反向传播
optimizer.zero_grad()  # 清空梯度
loss.backward()        # 计算梯度

# 更新模型参数
optimizer.step()

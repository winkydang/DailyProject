import torch
import torch.nn as nn
import torch.optim as optim

# 定义一个简单的线性模型
class SimpleLinearModel(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(SimpleLinearModel, self).__init__()
        # 定义线性层
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        # 实现前向传播
        return self.linear(x)


# L1正则化函数：计算变量（通常是模型参数）的L1范数（即其绝对值之和）
def l1_penalty(var):
    return torch.abs(var).sum()


# 定义超参数
input_dim = 10     # 输入特征的维度
output_dim = 1     # 输出的维度
l1_weight = 0.01   # L1正则化的权重
l2_weight = 0.01   # L2正则化的权重（通过weight_decay参数实现）
learning_rate = 0.01  # 学习率
num_epochs = 100   # 训练的总迭代次数

# 创建模型、损失函数和优化器
model = SimpleLinearModel(input_dim, output_dim)  # 实例化模型
criterion = nn.MSELoss()                          # 使用均方误差作为损失函数
# 使用SGD优化器，并通过weight_decay参数设置L2正则化的权重
optimizer = optim.SGD(model.parameters(), lr=learning_rate, weight_decay=l2_weight)

# 生成随机数据用于训练
x_train = torch.randn(100, input_dim)  # 生成100个样本，每个样本有input_dim个特征
y_train = torch.randn(100, output_dim)  # 生成100个标签

# 训练过程
for epoch in range(num_epochs):
    # 前向传播：通过模型计算预测值
    outputs = model(x_train)
    # 计算均方误差损失   # 后面loss.backward()才是执行反向传播
    loss = criterion(outputs, y_train)

    # 计算L1正则化损失
    l1_reg = torch.tensor(0., requires_grad=True)
    for name, param in model.named_parameters():
        if 'weight' in name:  # 仅对权重应用L1正则化，不对偏置应用  # name:'Linear.weight'      or  name:'Linear.weight'
            # l1_reg += l1_penalty(param)  # 报错：RuntimeError: a leaf Variable that requires grad is being used in an in-place operation.
            # 这个错误是因为当你对一个需要梯度的变量（在这里是l1_reg）执行原地操作时，PyTorch会抛出这个错误。原地操作会修改变量的值，而不是创建一个新的变量。这在反向传播计算中可能会导致问题，因为PyTorch需要原始值来正确地计算梯度。
            l1_reg = l1_reg + l1_penalty(param)
    # 将L1正则化损失添加到原始损失中
    loss += l1_weight * l1_reg

    # 反向传播：计算关于损失的梯度
    optimizer.zero_grad()  # 清零之前计算的梯度
    loss.backward()        # 执行反向传播
    optimizer.step()       # 更新模型参数

    # 每10个迭代打印一次损失
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}')

print("Training finished.")

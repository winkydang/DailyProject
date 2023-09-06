import torch
from torch import nn
from torch import optim


# 创建神经网络类
class Model(nn.Module):
    # 初始化参数
    def __init__(self):
        # 调用父类方法
        super(Model, self).__init__()
        # 创建第一层隐藏层
        self.linear1 = nn.Linear(2, 2)
        # 创建第二层隐藏层
        self.linear2 = nn.Linear(2, 2)

        # 初始化神经网络参数
        # 初始化权重
        self.linear1.weight.data = torch.tensor([[0.15, 0.20], [0.25, 0.30]])
        self.linear2.weight.data = torch.tensor([[0.40, 0.45], [0.50, 0.55]])
        # 初始化偏置
        self.linear1.bias.data = torch.tensor([0.35, 0.35])
        self.linear2.bias.data = torch.tensor([0.60, 0.60])

    # 前向传播方法
    def forward(self, x):
        print("执行了forward方法")
        # 数据经过第一层隐藏层
        x = self.linear1(x)
        # 计算第一层激活值
        x = torch.sigmoid(x)
        # 数据经过第二层隐藏层
        x = self.linear2(x)
        # 计算第二层激活值
        x = torch.sigmoid(x)
        return x


if __name__ == '__main__':
    # 创建x值
    inputs = torch.tensor([[0.05, 0.10]])
    # 创建y真实值
    target = torch.tensor([[0.01, 0.99]])

    # 实例化神经网络对象
    model = Model()
    # 模型预测,生成y预测值,此代码会执行forward方法
    output = model(inputs)
    print("output-->", output)

    # 计算误差
    loss = torch.sum((output - target) ** 2) / 2
    print("loss-->", loss)

    # 优化方法
    optimizer = optim.SGD(model.parameters(), lr=0.5)

    # 梯度清零
    optimizer.zero_grad()

    # 反向传播
    loss.backward()

    # 打印梯度值
    print("w1,w2,w3,w4-->", model.linear1.weight.grad.data)
    print("w5,w6,w7,w8-->", model.linear2.weight.grad.data)

    # 更新参数
    optimizer.step()

    # 打印神经网络参数
    print(model.state_dict())

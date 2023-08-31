import torch
from torch import nn


# 主要参数: reduction 计算模式可为none、sum、mean
    # none: 逐个元素计算
    # sum: 所有元素求和, 返回标量
    # mane: 加权平均, 返回标量
    # 默认计算加权平均值
def test():

    # 1 设置真实值和预测值
    y_pred = torch.tensor([1.0, 1.0, 1.9], requires_grad=True)
    y_true = torch.tensor([2.0, 2.0, 2.0], dtype=torch.float32)

    # 2 实例MAE损失对象
    loss = nn.MSELoss()

    # 3 计算损失
    my_loss = loss(y_pred, y_true)
    print('myloss--->', my_loss)  # myloss---> tensor(0.6700, grad_fn=<MseLossBackward0>)


test()
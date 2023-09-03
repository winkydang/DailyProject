import torch
from torch import nn


def test():

    # 1 设置真实值和预测值
    y_true = torch.tensor([[0], [1]])
    y_pred = torch.tensor ([[0.6], [0.4]], requires_grad=True)

    # 2 实例smmothL1损失对象
    loss = nn.SmoothL1Loss()

    # 3 计算损失
    my_loss = loss(y_pred, y_true)
    # my_loss.backward()
    print('myloss--->', my_loss)  # myloss---> tensor(0.1800, grad_fn=<SmoothL1LossBackward0>)

    # 手工验证：
    # 总损失：( 0.5*(0.6-0)^2 + 0.5*(0.4-1)^2 ) = (0.18+0.18) = 0.36
    mysquare = torch.square(torch.tensor([0.6, 0.6])) * 0.5
    my_loss2 = torch.mean(mysquare)
    print('2个样本，手工计算损失my_loss2--->', my_loss2.numpy())  # 2个样本，手工计算损失my_loss2---> 0.18


test()

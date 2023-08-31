import torch
from torch import nn


# APi功能 计算inputs与target之差的绝对值
# 主要参数: reduction 计算模式可为none、sum、mean
    # none: 逐个元素计算
    # sum: 所有元素求和, 返回标量
    # mean: 加权平均, 返回标量
    # 默认计算加权平均值
def test():

    # 1 设置真实值和预测值
    y_pred = torch.tensor([1.0, 1.0, 1.9], requires_grad=True)
    y_true = torch.tensor([2.0, 2.0, 2.0], dtype=torch.float32)

    # 2 实例MAE损失对象
    loss_ = nn.L1Loss()
    loss_mean = nn.L1Loss(reduction='mean')
    loss_sum = nn.L1Loss(reduction='sum')
    loss_none = nn.L1Loss(reduction='none')

    # 3 计算损失
    my_loss_ = loss_(y_pred, y_true)
    my_loss_mean = loss_mean(y_pred, y_true)
    my_loss_sum = loss_sum(y_pred, y_true)
    my_loss_none = loss_none(y_pred, y_true)
    print('my_loss_--->', my_loss_)  # my_loss_---> tensor(0.7000, grad_fn=<MeanBackward0>)
    print('my_loss_.item()--->', my_loss_.item())  # my_loss_.item()---> 0.699999988079071
    print('my_loss_mean--->', my_loss_mean)  # my_loss_mean---> tensor(0.7000, grad_fn=<MeanBackward0>)
    print('my_loss_sum--->', my_loss_sum)  # my_loss_sum---> tensor(2.1000, grad_fn=<SumBackward0>)
    print('my_loss_none--->', my_loss_none)  # my_loss_none---> tensor([1.0000, 1.0000, 0.1000], grad_fn=<AbsBackward0>)


test()
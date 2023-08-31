# 在处理二分类任务时，我们不再使用softmax激活函数，而是使用sigmoid激活函数，那损失函数也相应的进行调整，使用二分类的交叉熵损失函数
# 在pytorch中实现时使用nn.BCELoss()或者 nn.BCEWithLogitsLoss()，如下所示：
import torch
from torch import nn
import torch.nn.functional as F


# BCELoss()用法
def test01():
    # 1 设置真实值和预测值
    y_pred = torch.tensor([1.6901, -0.5459, -0.2469])
    # 两个类别:0和1
    y_true = torch.tensor([0, 1, 0], dtype=torch.float32)

    # 2 实例化二分类交叉熵损失
    criterion = nn.BCELoss()

    # 3 因是一个概率分布，在数据输入损失函数之前，需要经过一下Sigmoid来把输出值变成0~1之间
    y_sigmoide_pred = torch.sigmoid(y_pred)  # 注意 使用sigmoid, 不是softmax
    print('y_sigmoide_pred--->', y_sigmoide_pred, y_sigmoide_pred.shape)
    print('loss_input target--->', y_sigmoide_pred.shape, y_true.shape)

    # 4 计算损失
    my_loss = criterion(y_sigmoide_pred, y_true)
    print('my_loss--->', my_loss)


# BCEWithLogitsLoss()用法
def test02():
    # 1 设置真实值和预测值
    y_pred = torch.tensor([1.6901, -0.5459, -0.2469])
    y_true = torch.tensor([0, 1, 0], dtype=torch.float32)

    # 2 实例化二分类交叉熵损失
    criterion = nn.BCEWithLogitsLoss()

    # 3 计算损失 不需要再对y_pred加入Sigmoid函数
    my_loss = criterion(y_pred, y_true)
    print('my_loss--->', my_loss)

    # 4 手工验证
    # loss = - ylog(y^) - (1-y)log(1-y^)
    a1  = -0*F.math.log(0.8442) -(1-0)*F.math.log(1-0.8442) \
          -1*F.math.log(0.3668) -(1-1)*F.math.log(1-0.3668) \
          -0*F.math.log(0.4386) -(1-0)*F.math.log(1-0.4386)

    print('a1--->', a1)
    print('三个样本，a1/3--->', a1 / 3)



test01()
test02()
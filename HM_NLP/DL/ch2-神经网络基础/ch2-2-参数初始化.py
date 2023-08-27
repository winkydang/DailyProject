import torch
import torch.nn.functional as F
import torch.nn as nn


# 1. 均匀分布随机初始化
def test01():

    linear = nn.Linear(5, 3)  # linear: Linear(in_features=5, out_features=3, bias=True)
    # 从0-1均匀分布产生参数
    nn.init.uniform_(linear.weight)  # 均匀分布随机初始化
    print(linear.weight.data)
    # linear.weight.data
    # tensor([[0.0336, 0.8172, 0.5519, 0.9551, 0.4327],
    #         [0.8627, 0.3063, 0.2462, 0.1332, 0.4569],
    #         [0.9654, 0.5078, 0.6481, 0.1258, 0.1969]])


# 2. 固定初始化，固定为同一数值
def test02():

    linear = nn.Linear(5, 3)
    nn.init.constant_(linear.weight, 5)
    print(linear.weight.data)


# 3. 全0初始化
def test03():

    linear = nn.Linear(5, 3)
    nn.init.zeros_(linear.weight)
    print(linear.weight.data)


# 4. 全1初始化
def test04():

    linear = nn.Linear(5, 3)
    nn.init.ones_(linear.weight)
    print(linear.weight.data)


# 5. 正态分布随机初始化
def test05():

    linear = nn.Linear(5, 3)
    nn.init.normal_(linear.weight, mean=0, std=1)
    print(linear.weight.data)


# 6. kaiming 初始化
def test06():

    # kaiming 正态分布初始化
    linear = nn.Linear(5, 3)
    nn.init.kaiming_normal_(linear.weight)
    print(linear.weight.data)

    # kaiming 均匀分布初始化
    linear = nn.Linear(5, 3)
    nn.init.kaiming_uniform_(linear.weight)
    print(linear.weight.data)


# 7. xavier 初始化
def test07():

    # xavier 正态分布初始化
    linear = nn.Linear(5, 3)
    nn.init.xavier_normal_(linear.weight)
    print(linear.weight.data)

    # xavier 均匀分布初始化
    linear = nn.Linear(5, 3)
    nn.init.xavier_uniform_(linear.weight)
    print(linear.weight.data)


if __name__ == '__main__':
    test01()
    test02()
    test03()
    test04()
    test05()
    test06()
    test07()
# tensor([[0.5505, 0.3676, 0.4874, 0.3586, 0.5368],
#         [0.2564, 0.5342, 0.3959, 0.6335, 0.1201],
#         [0.4298, 0.0340, 0.7194, 0.9516, 0.2563]])
# tensor([[5., 5., 5., 5., 5.],
#         [5., 5., 5., 5., 5.],
#         [5., 5., 5., 5., 5.]])
# tensor([[0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.],
#         [0., 0., 0., 0., 0.]])
# tensor([[1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.],
#         [1., 1., 1., 1., 1.]])
# tensor([[-0.5679,  0.3937,  0.6449,  0.4220,  0.4920],
#         [-1.3258,  0.8684,  0.0775,  0.1583, -0.0231],
#         [-0.7278, -0.9334, -1.2458,  0.6468, -2.0402]])
# tensor([[ 0.1572,  0.1977, -0.5086, -0.9302,  0.1862],
#         [-0.5505,  0.8538,  0.8376,  0.4474, -1.4401],
#         [-1.7933,  0.2138, -0.1770,  0.7870,  0.0789]])
# tensor([[ 0.0472, -0.5575, -1.0640,  0.8712, -0.1330],
#         [ 1.0540,  0.8376, -1.0263, -0.8160, -0.1802],
#         [ 0.7210,  0.1894,  1.0851, -0.0359, -0.0648]])
# tensor([[-0.0107,  0.0110, -0.0581, -1.2355,  0.3405],
#         [ 0.4523, -0.8882,  0.6094,  0.4280, -1.1676],
#         [ 0.1729,  0.2201,  0.5475,  0.0195, -0.1549]])
# tensor([[-0.0247, -0.6535, -0.1642, -0.1494, -0.7446],
#         [-0.6806,  0.7991, -0.2871, -0.8494,  0.4508],
#         [ 0.8632, -0.1859,  0.6281,  0.1941,  0.3526]])

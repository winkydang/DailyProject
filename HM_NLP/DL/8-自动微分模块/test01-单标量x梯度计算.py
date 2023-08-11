# 自动微分（Autograd）模块对张量做了进一步的封装，具有自动求导功能
# 自动微分模块是构成神经网络训练的必要模块，在神经网络的反向传播过程中，Autograd模块基于正向计算的结果对当前的参数进行微分计算，从而实现网络权重参数的更新。
import torch

# 注意1 梯度：在一个点上，对函数求导，得到的值 就是梯度
# 注意2 梯度和梯度下降是两个不同的事
# 1 定义一个点
# 2 定义一个曲线
# 3 求导 自动微分
# 4 打印x的值 x的导数
# y'|(x=2) = 2 * (x ** 2)/x  = 4x|x=2 = 8
# y'|(x=10) = 2 * (x ** 2)/x  = 4x|x=10 = 40

# 单标量张量梯度计算
def test01():
    # 定义一个标量张量(点)
    # requires_grad=:默认为False,不会自动计算梯度;为True的话是将自动计算的梯度值保存到grad中
    x = torch.tensor(10, requires_grad=True, dtype=torch.float32)  # x: tensor(10., requires_grad=True)
    print("x-->", x)
    print(id(x))  # 5449220560
    # 定义一个曲线
    y = 2 * x ** 2  # y: tensor(200., grad_fn=<MulBackward0>)
    print("y-->", y)  # y--> tensor(200., grad_fn=<MulBackward0>)

    # 计算x点的梯度
    # 此时y是一个标量,可以不用使用y.sum()转换成标量
    print("y.sum()-->", y.sum())  # y.sum()--> tensor(200., grad_fn=<SumBackward0>)
    # y'|(x=10) = (2*x**2)'|(x=10) = 4x|(x=10) = 40
    y.sum().backward()

    # 打印x的梯度值
    print("x的梯度值是:", x.grad)  # x的梯度值是: tensor(40.)

    # 梯度下降公式更新x值
    # x1 = x0 - r*△ (r是步长, △是x0点的梯度)
    # x.data是修改开始x内存中的内部数据,前后x的内存空间一样;如果使用x,此时前后x的内存空间不同
    x.data = x.data - 0.001 * x.grad
    # 打印更新后的x值
    print(x)  # tensor(9.9600, requires_grad=True)
    print(id(x))  # 5449220560


if __name__ == '__main__':
    test01()



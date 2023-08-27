import torch


# 多标量张量梯度计算
def test03():
    # 定义两个标量张量
    x1 = torch.tensor(10, requires_grad=True, dtype=torch.float64)  # x1: tensor(10., dtype=torch.float64, requires_grad=True)
    x2 = torch.tensor(20, requires_grad=True, dtype=torch.float64)
    # print(x1.grad)  # None
    # print(x2.grad)  # None

    # 定义一个曲线
    y = x1 ** 2 + x2 ** 2 + x1 * x2
    print(y)  # tensor(700., dtype=torch.float64, grad_fn=<AddBackward0>)

    # 将输出结果变为标量
    y = y.sum()
    # print(y.sum())  # y.sum(): tensor(700., dtype=torch.float64, grad_fn=<SumBackward0>)
    # print(y.sum)  # <built-in method sum of Tensor object at 0x135ce0860>

    # 自动微分(计算梯度)
    # 计算x1点的梯度, 此时x2为常量
    # y'|(x1=10) = (x1**2+40+x1*20)'|(x1=10) = (2*x1+20)|(x1=10) = 40
    # 计算x2点的梯度, 此时x1为常量
    # y'|(x2=20) = (20+x2**2+10*x2)'|(x2=20) = (2*x2+10)|(x2=20) = 50
    y.backward()

    # 打印两个变量的梯度
    print("x1.grad-->", x1.grad)  # x1.grad--> tensor(40., dtype=torch.float64)
    print("x2.grad-->", x2.grad)  # x2.grad--> tensor(50., dtype=torch.float64)


if __name__ == '__main__':
    test03()
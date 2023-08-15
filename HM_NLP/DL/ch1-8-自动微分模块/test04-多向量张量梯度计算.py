import torch


# 多向量张量梯度计算
def test04():
    # 定义两个向量张量
    x1 = torch.tensor([10, 20], requires_grad=True, dtype=torch.float64)
    x2 = torch.tensor([30, 40], requires_grad=True, dtype=torch.float64)

    # 定义一个曲线
    y = x1 ** 2 + x2 ** 2 + x1 * x2
    print("y-->", y)  # y--> tensor([1300., 2800.], dtype=torch.float64, grad_fn=<AddBackward0>)

    # 将输出结果变为标量
    y = y.sum()
    print("y.sum()-->", y)  # y.sum()--> tensor(4100., dtype=torch.float64, grad_fn=<SumBackward0>)

    # 自动微分(计算梯度)
    # 计算x1点的梯度, 此时x2为常量
    # y'|(x1=10,x2=30) = (x1**2+900+x1*30)'|(x1=10,x2=30) = (2*x1+30)|(x1=10,x2=30) = 50
    # y'|(x1=20,x2=40) = (x1**2+1600+x1*40)'|(x1=20,x2=40) = (2*x1+40)|(x1=20,x2=40) = 80
    # 计算x2点的梯度, 此时x1为常量
    # y'|(x2=30,x1=10) = (100+x2**2+10*x2)'|(x2=30,x1=10) = (2*x2+10)|(x2=30,x1=10) = 70
    # y'|(x2=40,x1=20) = (400+x2**2+20*x2)'|(x2=40,x1=20) = (2*x2+20)|(x2=40,x1=20) = 100
    y.backward()

    # 打印两个张量的梯度
    print("x1.grad-->", x1.grad)  # x1.grad--> tensor([50., 80.], dtype=torch.float64)

    print("x2.grad-->", x2.grad)  # x2.grad--> tensor([ 70., 100.], dtype=torch.float64)


if __name__ == '__main__':
    test04()
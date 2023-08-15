import torch


# 单向量张量梯度计算
def test02():
    # 定义一个向量张量(点)
    x = torch.tensor([10, 20], requires_grad=True, dtype=torch.float32)
    print("x-->", x)  # x--> tensor([10., 20.], requires_grad=True)
    # print(x.grad)  # None

    # 定义一个曲线
    y = 2 * x ** 2
    print("y-->", y)  # y--> tensor([200., 800.], grad_fn=<MulBackward0>)
    print(y.sum())  # tensor(1000., grad_fn=<SumBackward0>)

    # 计算梯度
    # x和y都是向量张量,不能进行求导,需要将y转换成标量张量-->y.sum()
    # y'|(x=10) = (2*x**2)'|(x=10) = 4x|(x=10) = 40
    # y'|(x=20) = (2*x**2)'|(x=20) = 4x|(x=20) = 80
    y.sum().backward()

    # 打印x的梯度
    print("x.grad-->", x.grad)  # x.grad--> tensor([40., 80.])



if __name__ == '__main__':
    test02()
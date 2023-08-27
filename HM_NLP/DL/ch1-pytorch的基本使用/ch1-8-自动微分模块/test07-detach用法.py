import torch

# 1. detach 函数用法  # detach 之后会产生一个新的张量, 新的张量作为叶子结点，并且该张量和原来的张量共享数据, 但是分离后的张量不需要计算梯度。
def test01():

    x = torch.tensor([10, 20], requires_grad=True, dtype=torch.float64)

    # Can't call numpy() on Tensor that requires grad. Use tensor.detach().numpy() instead.
    # print(x.numpy())  # 错误
    print(x.detach().numpy())  # 正确  # 需要先使用 detach 函数将张量进行分离, 再使用 numpy 函数


# 2. detach 前后张量共享内存
def test02():

    x1 = torch.tensor([10, 20], requires_grad=True, dtype=torch.float64)

    # x2 作为叶子结点
    x2 = x1.detach()

    # 两个张量的值一样: 140421811165776 140421811165776
    print(id(x1.data), id(x2.data))
    print(x1)  # tensor([10., 20.], dtype=torch.float64, requires_grad=True)
    print(x2)  # tensor([10., 20.], dtype=torch.float64)
    x2.data = torch.tensor([100, 200])
    print(x1)  # tensor([10., 20.], dtype=torch.float64, requires_grad=True)
    print(x2)  # tensor([100, 200])

    # x2 不会自动计算梯度: False
    print(x2.requires_grad)  # False


if __name__ == '__main__':
    test01()
    test02()

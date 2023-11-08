import torch  # 需要安装torch模块,虚拟环境中已经安装好了
import numpy as np


# 1. 根据已有数据创建张量
def test01():

    # 1. 创建张量标量
    data = torch.tensor(10)
    print(data)
    # 查看基本数据类型
    print(type(data))
    # 查看cpu张量数据类型
    print(data.type())
    # 查看张量数据类型
    print(data.dtype)

    # 2. numpy 数组, 由于 data 为 float64, 下面代码也使用该类型
    data = np.random.randn(2, 3)
    data = torch.tensor(data)
    print(data)

    # 3. 列表, 下面代码使用默认元素类型 float32
    data = [[10., 20., 30.], [40., 50., 60.]]
    data = torch.tensor(data)
    print(data)


# 2. 创建指定形状的张量
def test02():

    # 1. 创建2行3列的张量, 默认 dtype 为 float32
    data = torch.Tensor(2, 3)
    print(data)

    # 2. 注意: 如果传递列表, 则创建包含指定元素的张量
    data = torch.Tensor([10])
    print(data)

    data = torch.Tensor([10, 20])
    print(data)


# 3. 使用具体类型的张量
def test03():

    # 1. 创建2行3列, dtype 为 int32 的张量
    data = torch.IntTensor(2, 3)
    print(data)

    # 2. 注意: 如果传递的元素类型不正确, 则会进行类型转换
    data = torch.IntTensor([2.5, 3.3])
    print(data)

    # 3. 其他的类型
    data = torch.ShortTensor()  # int16
    data = torch.LongTensor()   # int64
    data = torch.FloatTensor()  # float32
    data = torch.DoubleTensor() # float64


if __name__ == '__main__':
    test01()
    # test02()
    # test03()
import torch

"""
可以通过一些方法使得在 requires_grad=True 的张量在某些时候计算不进行梯度计算。
如：
1. with torch.no_grad():
2. 装饰器 
    @torch.no_grad()
    def my_func(x):
3. torch.set_grad_enabled(False) 
"""


# 控制不计算梯度
def dm_torch_no_grad():

    x = torch.tensor(10, requires_grad=True, dtype=torch.float64)
    print(x.requires_grad)  # True

    # 第一种方式: 对代码进行装饰
    with torch.no_grad():
        y = x ** 2  # tensor(100., dtype=torch.float64)
    print(y.requires_grad)  # False

    # 第二种方式: 对函数进行装饰
    @torch.no_grad()
    def my_func(x):
        return x ** 2
    print(my_func(x).requires_grad)  # False

    # 第三种方式
    torch.set_grad_enabled(False)
    y = x ** 2
    print(y.requires_grad)  # False

dm_torch_no_grad()
# 运行结果：
# True
# False
# False
# False

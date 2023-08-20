# 函数 test06求函数极小值() 思路分析
# 求y = x ** 2 + 20的极小值点 并打印y是最小值时 w的值、梯度
# 1 定义点x=10 requires_grad=True  dtype=torch.float32
# 2 定义函数 y = x ** 2 + 20
# 3 利用梯度下降法 循环迭代1000 求最优解
# 3-1 正向计算(前向传播)
# 3-2 梯度清零 x.grad.zero_() 如果不清零x.grad是累加的梯度值
# 3-3 反向传播
# 3-4 梯度更新 x.data = x.data - 0.01 * x.grad
# 其他辅助信息
# print('开始 权重x初始值:%.6f (0.01 * x.grad):无 y:%.6f' %(x, y))
# print('次数:%d 权重x: %.6f, (0.01 * x.grad):%.6f y:%.6f' %(i, x, 0.01*x.grad, y))
import torch

def test06():

    # 1 定义点x=10 requires_grad=True  dtype=torch.float32
    x = torch.tensor(10, requires_grad=True, dtype=torch.float32)   # x: tensor(10., requires_grad=True)

    # 2 定义函数 y = x ** 2 + 20
    y = x ** 2 + 20  # tensor(120., grad_fn=<AddBackward0>)
    print('开始 权重x初始值:%.6f (0.01 * x.grad):无 y:%.6f' %(x, y))
    # 开始 权重x初始值:10.000000 (0.01 * x.grad):无 y:120.000000

    # 3 利用梯度下降法 循环迭代1000 求最优解
    for i in range(1, 1000+1):

        # 3-1 正向计算(前向传播)
        y = x ** 2 + 20

        # 3-2 梯度清零 x.grad.zero_()
        # 默认张量的 grad 属性会累计历史梯度值 需手工清零上一次的提取
        # 一开始梯度不存在, 需要做判断
        if x.grad is not None:
            x.grad.zero_()

        # 3-3 反向传播
        y.backward()

        # 3-4 梯度更新 x.data = x.data - 0.01 * x.grad
        x.data = x.data - 0.01 *x.grad  # 注 x = x - 0.01*x.grad  # 使用梯度x.grad更新x的值x.data

        print('次数:%d 权重x: %.6f, (0.01 * x.grad):%.6f y:%.6f' % (i, x, 0.01 * x.grad, y))
        # 次数:1 权重x: 9.800000, (0.01 * x.grad):0.200000 y:120.000000
        # 次数:2 权重x: 9.604000, (0.01 * x.grad):0.196000 y:116.040001
        # 次数:3 权重x: 9.411921, (0.01 * x.grad):0.192080 y:112.236816
        # 次数:639 权重x: 0.000025, (0.01 * x.grad):0.000001 y:20.000000
        # 次数:640 权重x: 0.000024, (0.01 * x.grad):0.000000 y:20.000000
        # 次数:999 权重x: 0.000000, (0.01 * x.grad):0.000000 y:20.000000
        # 次数:1000 权重x: 0.000000, (0.01 * x.grad):0.000000 y:20.000000

    print('x：', x, x.grad,  'y最小值', y)
    # x： tensor(1.6830e-08, requires_grad=True) tensor(3.4346e-08) y最小值 tensor(20., grad_fn=<AddBackward0>)


if __name__ == '__main__':
    test06()

import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F

font = {'family': 'Arial Unicode MS', 'size': 12}
plt.rc('font', **font)

def test():
    # 创建画布和坐标轴
    _, axes = plt.subplots(1, 2)  # plt.subplots(1, 2) creates a figure with one row and two columns of subplots.
    # The first value returned by plt.subplots() (which is represented by _) is typically ignored or discarded because it refers to the figure.
    # The second value returned by plt.subplots() (which is represented by axes) is a NumPy array containing references to the subplot axes. In this case, you'll have two axes objects in the array, one for each subplot.
    # You can then use the axes array to plot data on each subplot,

    # 函数图像
    x = torch.linspace(-20, 20, 1000)  # x.shape: 1000
    # 输入值x通过sigmoid函数转换成激活值y
    y = F.sigmoid(x)
    axes[0].plot(x, y)
    axes[0].grid()
    axes[0].set_title('Sigmoid 函数图像')

    # 导数图像
    x = torch.linspace(-20, 20, 1000, requires_grad=True)
    torch.sigmoid(x).sum().backward()

    # x.detach():输入值x的ndarray数组
    # x.grad:计算梯度，求导
    axes[1].plot(x.detach(), x.grad)
    axes[1].grid()
    axes[1].set_title('Sigmoid 导数图像')

    plt.show()


if __name__ == '__main__':
    test()

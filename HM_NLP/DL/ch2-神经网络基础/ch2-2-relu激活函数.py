import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F

font = {'family': 'Arial Unicode MS', 'size': 12}
plt.rc('font', **font)

def test():
    _, axes = plt.subplots(1, 2)

    # 函数图像
    x = torch.linspace(-20, 20, 1000)
    y = F.relu(x)
    axes[0].plot(x, y)
    axes[0].grid()
    axes[0].set_title('Tanh 函数图像')

    # 导数图像
    x = torch.linspace(-20, 20, 1000, requires_grad=True)
    torch.relu(x).sum().backward()

    axes[1].plot(x.detach(), x.grad)
    axes[1].grid()
    axes[1].set_title('Tanh 导数图像')

    plt.show()


if __name__ == '__main__':
    test()
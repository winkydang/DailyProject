import torch
import matplotlib.pyplot as plt


ELEMENT_NUMBER = 30


# 1. 实际平均温度
def test01():

    # 固定随机数种子
    torch.manual_seed(0)

    # 产生30天的随机温度
    temperature = torch.randn(size=[ELEMENT_NUMBER,]) * 10
    print(temperature)

    # 绘制平均温度
    days = torch.arange(1, ELEMENT_NUMBER + 1, 1)
    plt.plot(days, temperature, color='r')
    plt.scatter(days, temperature)
    plt.show()


# 2. 指数加权平均温度
def test02(beta=0.9):

    # 固定随机数种子
    torch.manual_seed(0)

    # 产生30天的随机温度
    temperature = torch.randn(size=[ELEMENT_NUMBER,]) * 10
    print(temperature)

    exp_weight_avg = []
    # idx从1开始
    for idx, temp in enumerate(temperature, 1):  # 索引idx从1开始

        # 第一个元素的的 EWA 值等于自身
        if idx == 1:
            exp_weight_avg.append(temp)
            continue

        # 第二个元素的 EWA 值等于上一个 EWA 乘以 β + 当前气温乘以 (1-β)
        # idx-2：2-2=0，exp_weight_avg列表中第一个值的下标值
        new_temp = exp_weight_avg[idx - 2] * beta + (1 - beta) * temp
        exp_weight_avg.append(new_temp)


    days = torch.arange(1, ELEMENT_NUMBER + 1, 1)
    plt.plot(days, exp_weight_avg, color='r')
    plt.scatter(days, temperature)
    plt.show()


if __name__ == '__main__':

    test01()
    test02(0.5)
    test02(0.9)

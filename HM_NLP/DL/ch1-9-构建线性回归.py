"""
    本小节我们主要手动构建数据集，假设函数，训练函数等来练习下对 PyTorch 相关API的使用。
"""
import torch
from sklearn.datasets import make_regression  # 创建线性模型数据集模块
import matplotlib.pyplot as plt
import random

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 创建数据集函数
def create_dataset():
    # 返回的x是二维数组(ndarray),y是一维数组(ndarray),coef是线性模型的系数(y=wx+b w=coef, b=bias)
    x, y, coef = make_regression(n_samples=100,  # 样本数
                                 n_features=1,  # 样本特征数
                                 noise=10,  # 噪音值,样本的标准差
                                 coef=True,  # 是否返回线性模型的系数
                                 bias=14.5,  # 线性模型的截距
                                 random_state=0)  # 随机数种子
    print('type(x): ', type(x), 'x.shape: ', x.shape)  # type(x):  <class 'numpy.ndarray'> x.shape:  (100, 1)
    print('type(y): ', type(y), 'y.shape: ', y.shape)  # type(y):  <class 'numpy.ndarray'> y.shape:  (100,)
    # ndarray转换成张量
    x = torch.tensor(x)  # 没转换为tensor前x是ndarray类型的
    y = torch.tensor(y)
    print('type(x): ', type(x), 'x.shape: ', x.shape)  # type(x):  <class 'torch.Tensor'> x.shape:  torch.Size([100, 1])
    print('type(y): ', type(y), 'y.shape: ', y.shape)  # type(y):  <class 'torch.Tensor'> y.shape:  torch.Size([100])
    return x, y, coef


# 构建数据加载器
# 每次进行模型训练时,采用批量数据集训练方式,需要对每次的所有数据集进行分组分批量训练,每组的数据集样本不能重复训练
def data_loader(x, y, batch_size):
    """
        样本数据分批生成器
        :param x: 特征值
        :param y: 目标值
        :param batch_size: 批量样本数
        """
    # 计算样本总个数
    data_len = len(y)
    # 生成样本数据索引值列表,根据索引值获取样本
    data_index = list(range(data_len))
    # 将样本索引值乱序
    random.shuffle(data_index)
    # 计算每次训练样本批数,保留整数部分
    batch_number = data_len // batch_size

    # 获取每批数据的x和y
    for idx in range(batch_number):
        # 每批数据起始索引值
        start = idx * batch_size
        # 每批数据结束索引值
        end = start + batch_size
        # 获取每批样本数据的x值
        batch_train_x = x[data_index[start:end]]
        # 获取每批样本数据的y值
        batch_train_y = y[data_index[start:end]]

        # 生成器,下一次循环会从上一次的结束位置开始,每次只取一个值,不会重复取值
        yield batch_train_x, batch_train_y


# 创建假设函数的w和b模型参数,两个可以自动微分的张量,
# 后续是要通过反向传播计算w和b的梯度,通过梯度下降法更新下一个w和b
w = torch.tensor(0.1, requires_grad=True, dtype=torch.float64)  # tensor(0.1000, dtype=torch.float64, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True, dtype=torch.float64)  # tensor(0., dtype=torch.float64, requires_grad=True)


# 创建假设函数
def linear_regression(x):
    y = w * x + b
    return y


# 创建损失函数
def square_loss(y_pred, y_true):
    """
        计算损失值函数
        :param y_pred: y的预测值
        :param y_true: y的真实值
        :return: 平方损失
        """
    return (y_pred - y_true) ** 2


# 创建更新w和b函数
def sgd(batch_size, learning_rate=0.01):
    """
        优化w和b参数函数
        :param batch_size: 使用批量样本的平均梯度,为批量样本数量
        :param learning_rate: 学习率,默认为0.01
        """
    w.data = w.data - learning_rate * w.grad / batch_size
    b.data = b.data - learning_rate * b.grad / batch_size


# 训练模型
def train():
    # 获取数据集
    x, y, coef = create_dataset()  # # 返回的x是二维数组(ndarray),y是一维数组(ndarray),coef是线性模型的系数(y=wx+b w=coef, b=bias)
    # 定义训练参数, 训练次数和学习率
    epochs, learning_rate = 100, 0.01
    # 存储损失值, 每次训练损失值, 总损失值
    epoch_loss, total_loss = [], 0
    # 统计训练样本数
    train_sample = 0
    # 循环遍历进行训练
    for _ in range(epochs):
        # 每次训练进行迭代训练
        for train_x, train_y in data_loader(x, y, 16):
            # 模型训练
            y_pred = linear_regression(train_x)
            # 计算损失值
            # 每批次总损失值
            # train_y.reshape(-1,1):保证y_true和y_pred形状一致
            loss = square_loss(y_pred, train_y.reshape(-1, 1)).sum()
            # 计算每次训练的总损失值
            # loss是一个张量,loss.item()获取张量中的损失值
            total_loss += loss.item()
            # 统计多少个样本数据进行了模型训练
            train_sample += len(train_y)

            # 梯度清零
            if w.grad is not None:
                w.grad.zero_()
            if b.grad is not None:
                b.grad.zero_()
            # 计算梯度值,反向传播
            loss.backward()
            # 更新梯度值
            sgd(16, learning_rate)  # 梯度下降法更新 w 和 b 的值
            print('loss: %.10f' % (total_loss / train_sample))
        # 保存每次迭代训练的损失值, 100次训练结果的损失值
        epoch_loss.append(total_loss / train_sample)

    # 查看真实模型和训练模型的系数,w是张量,通过.data.item()获取张量中的系数值
    print(coef, w.item())  # 42.38550485581797 42.69298939437004
    print(b.item())  # 13.733376403360259
    # 绘制真实数据样本分布图
    plt.scatter(x, y)

    # 创建特征值的等差张量
    x = torch.linspace(x.min(), x.max(), 1000)
    # 14.5为y=wx+b中的截距值
    # 创建训练模型的目标值张量
    y1 = torch.tensor([v * w + 14.5 for v in x])
    # 创建真实模型的目标值张量
    y2 = torch.tensor([v * coef + 14.5 for v in x])

    # 绘制训练模型和真实模型
    font = {'family': 'Arial Unicode MS', 'size': 12}
    plt.rc('font', **font)
    plt.plot(x, y1, label='训练')
    plt.plot(x, y2, label='真实')
    plt.grid()
    plt.legend()
    plt.show()

    # 打印损失变化曲线
    plt.plot(range(epochs), epoch_loss)
    plt.title('损失变化曲线')
    plt.grid()
    plt.show()

train()

# 在多分类任务通常使用softmax将logits转换为概率的形式，所以多分类的交叉熵损失也叫做softmax损失
import torch
from torch import nn
import torch.nn.functional as F


# nn.CrossEntropyLoss()
def test01():
    # 对于nn.CrossEntropyLoss()来说，损失函数内部自带softmax，所以不需要人为额外在上一步执行softmax操作
    # 设置真实值和预测值
    # 目标值（标签）编码分类：
    # label encode标签编码,将类别转换成从0开始的整数 (例如:中杯,大杯,超大杯 对应 0, 1, 2)
    # one-hot encode独热编码,将类别转换成0,1,在1位置上就代表此类别 (例如:中杯->1,0,0 大杯->0,1,0 超大杯->0,0,1)
    # y_true = torch.tensor([[0, 1, 0], [0, 0, 1]], dtype=torch.long)
    # api计算损失值时会自动的将真实值y转换成 one-hot 独热编码格式
    # [1,2]是label enconde格式,此时还有一个0类,是三分类问题
    y_true = torch.tensor([1, 2], dtype=torch.long)
    # 预测值y每个数据由三个维度组成,因为是三分类问题,每个维度通过softmax转换代表当前类别的概率
    y_pred = torch.tensor([[1.04, 1.95, 1.01], [1.1, 1.8, 1.1]], dtype=torch.float32)

    print('y_true--->', y_true, y_true.shape)
    print('y_pred--->', y_pred, y_pred.shape)

    # 实例化交叉熵损失
    loss1 = nn.CrossEntropyLoss()  # 默认求平均损失
    # loss1 = nn.CrossEntropyLoss(reduction='sum')
    # 计算损失结果
    my_loss1 = loss1(y_pred, y_true).numpy()
    print('nn.CrossEntropyLoss(): my_loss1--->', my_loss1)  # nn.CrossEntropyLoss(): my_loss1---> 0.98685086


# nn.NLLLoss()
def test02():
    # nn.NLLLoss() 和 LogSoftmax() 相结合进行交叉熵损失计算
    # 对预测值先进行softmax，然后再log；最后再调用nn.NLLLoss()
    # 设置真实值和预测值
    y_true = torch.tensor([1, 2], dtype=torch.long)
    # 预测值y每个数据由三个维度组成,因为是三分类问题,每个维度通过softmax转换代表当前类别的概率
    y_pred = torch.tensor([[1.04, 1.95, 1.01], [1.1, 1.8, 1.1]], dtype=torch.float32)

    # 实例化交叉熵损失：仅仅实现负号的功能
    loss2 = nn.NLLLoss()
    # loss2 = nn.NLLLoss(reduction='sum')
    # 计算损失结果
    my_loss2 = loss2(F.log_softmax(y_pred, dim=-1), y_true).numpy()
    print('nn.NLLLoss(): my_loss2--->', my_loss2)  # nn.NLLLoss(): my_loss2---> 0.98685086

    # 手工验算
    print('-' * 50)
    print(torch.softmax(y_pred, dim=-1))
    # tensor([[0.2245, 0.5577, 0.2178],
    #         [0.2491, 0.5017, 0.2491]])

    # 手工验证1 : log以e为底 不是log以10为底
    # -( (0*log0.2245 + 1*log0.5577 + 0*log0.2178) + (0*log0.2491 + 0*log0.5017 + 1*log0.2491) )
    a = - ((0 * F.math.log(0.2245) + 1 * F.math.log(0.5577) + 0 * F.math.log(0.2178)) + \
           (0 * F.math.log(0.2491) + 0 * F.math.log(0.5017) + 1 * F.math.log(0.2491)))
    print('\n手工验证1 损失a--->', a, 'log以e为底')  # 1.9738349523006313
    print('\n手工验证1 平均损失a--->', a / 2, 'log以e为底')  # 0.9869174761503157


test01()
test02()

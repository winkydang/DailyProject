# 位置编码器类PositionalEncoding 实现思路分析
# 1 init函数  (self, d_model, dropout, max_len=5000)
#   super()函数 定义层self.dropout
#   定义位置编码矩阵pe  定义位置列-矩阵position 定义变化矩阵div_term
#   套公式div_term = torch.exp(torch.arange(0, d_model, 2) * -(math.log(10000.0)/d_model))
#   位置列-矩阵 * 变化矩阵 阿达码积my_matmulres
#   给pe矩阵偶数列奇数列赋值 pe[:, 0::2] pe[:, 1::2]
#   pe矩阵注册到模型缓冲区 pe.unsqueeze(0)三维 self.register_buffer('pe', pe)
# 2 forward(self, x) 返回self.dropout(x)
#   给x数据添加位置特征信息 x = x + Variable( self.pe[:,:x.size()[1]], requires_grad=False)
import math

import torch
from torch import nn


class Embeddings(nn.Module):
    def __init__(self, d_model, vocab):
        # 参数d_model 每个词汇的特征尺寸 词嵌入维度
        # 参数vocab   词汇表大小
        super(Embeddings, self).__init__()
        self.d_model = d_model
        self.vocab = vocab

        # 定义词嵌入层
        self.lut = nn.Embedding(self.vocab, self.d_model)

    def forward(self, x):
        # 将x传给self.lut并与根号下self.d_model相乘作为结果返回
        # x经过词嵌入后 增大x的值, 词嵌入后的embedding_vector+位置编码信息,值量纲差差不多
        return self.lut(x) * math.sqrt(self.d_model)


class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout, max_len=5000):
        # 参数d_model 词嵌入维度 eg: 512个特征
        # 参数max_len 单词token个数 eg: 60个单词  # max_len（序列的最大长度，默认为 5000）
        # dropout（dropout层的比率
        super(PositionalEncoding, self).__init__()

        # 定义dropout层  # 初始化 Dropout 层 使用 nn.Dropout 创建一个 dropout 层，这有助于减少过拟合。
        self.dropout = nn.Dropout(p=dropout)

        # 思路：位置编码矩阵 + 特征矩阵 相当于给特征增加了位置信息
        # 定义位置编码矩阵PE eg pe[60, 512], 位置编码矩阵和特征矩阵形状是一样的
        pe = torch.zeros(max_len, d_model)  # 创建一个形状为 (max_len, d_model) 的零矩阵 pe，用于存储位置编码。

        # 定义位置列-矩阵position  数据形状[max_len,1] eg: [0,1,2,3,4...60]^T
        position = torch.arange(0, max_len).unsqueeze(1)  # 使用 arange 和 unsqueeze 生成一个代表各个位置的列向量
        print('position--->', position.shape, position)

        # 定义变化矩阵div_term [1,256]     # 计算一个用于调整位置编码的变化矩阵 div_term。
        # torch.arange(start=1, end=512, 2)结果并不包含end。在start和end之间做一个等差数组 [0, 2, 4, 6 ... 510]
        div_term = torch.exp(torch.arange(0, d_model, 2) * -(math.log(10000.0) / d_model))

        # 位置列-矩阵 @ 变化矩阵 做矩阵运算 [60*1]@ [1*256] ==> 60 *256
        # 矩阵相乘也就是行列对应位置相乘再相加，其含义，给每一个列属性（列特征）增加位置编码信息  # 使用矩阵乘法将位置信息加入到 div_term 中。
        my_matmulres = position * div_term
        # print('my_matmulres--->', my_matmulres.shape, my_matmulres)

        # 在位置编码矩阵的偶数列上应用正弦函数，在奇数列上应用余弦函数，赋值给pe位置编码矩阵，得到的pe矩阵的shape是[60,512]
        # 给位置编码矩阵奇数列，赋值sin曲线特征
        pe[:, 0::2] = torch.sin(my_matmulres)
        # 给位置编码矩阵偶数列，赋值cos曲线特征
        pe[:, 1::2] = torch.cos(my_matmulres)

        # 形状变化 [60,512]-->[1,60,512]
        pe = pe.unsqueeze(0)

        # 把pe位置编码矩阵 注册成模型的持久缓冲区buffer; 模型保存再加载时，可以跟模型参数一样，一同被加载
        # 什么是buffer: 对模型效果有帮助的，但是却不是模型结构中超参数或者参数，不参与模型训练
        self.register_buffer('pe', pe)  # 使用 register_buffer 方法将位置编码矩阵 pe 注册为模型的持久缓冲区。

    # forward 方法定义了如何对输入数据应用位置编码。它将位置编码添加到输入张量 x 上，并应用 dropout。
    def forward(self, x):
        # 注意：输入的x形状2*4*512  pe是1*60*512 形状 如何进行相加
        # 只需按照x的单词个数 给特征增加位置信息
        # x = x + Variable(self.pe[:,:x.size()[1]], requires_grad=False)
        # x = x + torch.Tensor(self.pe[:,:x.size()[1]])  # 使用Tensor定义变量时就不用使用requires_grad=False属性了
        x = x + torch.tensor(self.pe[:,:x.size()[1]], requires_grad=False)  # 想使用requires_grad的话使用小写't'的torch.tensor()定义张量
        return self.dropout(x)


# nn.Dropout演示
print('--'*10, 'nn.Dropout演示')
m = nn.Dropout(p=0.2)
input = torch.randn(4, 5)
output = m(input)
print(output)
print(type(output))

# torch.unsqueeze演示
print('--'*10, 'torch.unsqueeze演示')
x = torch.tensor([1, 2, 3, 4])
print(x)
# tensor([1, 2, 3, 4])
print(torch.unsqueeze(x, 0))
# tensor([[ 1,  2,  3,  4]])
print(torch.unsqueeze(x, 1))
# tensor([[ 1],
#         [ 2],
#         [ 3],
#         [ 4]])

# 调用PositionalEncoding
print('--'*10, '调用PositionalEncoding')
def dm_test_PositionalEncoding():

    d_model = 512  # 词嵌入维度是512维
    vocab = 1000  # 词表大小是1000

    # 1 实例化词嵌入层
    my_embeddings = Embeddings(d_model, vocab)

    # 2 让数据经过词嵌入层 [2,4] --->[2,4,512]
    x = torch.LongTensor(torch.LongTensor([[100, 2, 421, 508], [491, 998, 1, 221]]))
    embed = my_embeddings(x)
    # print('embed--->', embed.shape)

    # 3 创建pe位置矩阵 生成位置特征数据[1,60,512]
    my_pe = PositionalEncoding(d_model=d_model, dropout=0.1, max_len=60)

    # 4 给词嵌入数据embed 添加位置特征 [2,4,512] ---> [2,4,512]
    pe_result = my_pe(embed)
    print('pe_result.shape--->', pe_result.shape)
    print('pe_result--->', pe_result)
dm_test_PositionalEncoding()

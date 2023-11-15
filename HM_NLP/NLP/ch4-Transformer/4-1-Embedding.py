# 无论是源文本嵌入还是目标文本嵌入，都是为了将文本中词汇的数字表示转变为向量表示, 希望在这样的高维空间捕捉词汇间的关系.
# 导入必备的工具包
import torch

# 预定义的网络层torch.nn, 工具开发者已经帮助我们开发好的一些常用层,
# 比如，卷积层, lstm层, embedding层等, 不需要我们再重新造轮子.
import torch.nn as nn

# 数学计算工具包
import math

# torch中变量封装函数Variable.
from torch.autograd import Variable

# Embeddings类 实现思路分析
# 1 init函数 (self, d_model, vocab)
    # 设置类属性 定义词嵌入层 self.lut层
# 2 forward(x)函数
    # self.lut(x) * math.sqrt(self.d_model)


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


# 然后创建Embeddings类的实例
embedding_layer = Embeddings(d_model=3, vocab=10)

# 接着创建输入数据
input_data = torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]])  # 这些数字表示词汇在词表中的索引。词嵌入的作用就是将文本中词汇的数字表示转变为向量表示

# 最后通过Embeddings实例来得到嵌入向量
embedded_input = embedding_layer(input_data)
print(embedded_input)
print(type(embedded_input))  # 查看类型，  <class 'torch.Tensor'>
print(embedded_input.shape)  # 查看tensor的形状大小，，torch.Size([2, 4, 3])


# embedding = nn.Embedding(10, 3)
# input = torch.LongTensor([[1,2,4,5],[4,3,2,9]])
# print(embedding(input))










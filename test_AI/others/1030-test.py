# import torch
#
# # 定义批量大小、序列长度和维度
# batch_size, seq_size, dim = 2, 3, 4
#
# # 生成一个随机的张量，维度为 (batch_size, seq_size, dim)
# embedding = torch.randn(batch_size, seq_size, dim)
#
# # 初始化一个LayerNorm层，指定归一化的维度为dim，并设置elementwise_affine为False（这意味着不使用可学习的参数）
# layer_norm = torch.nn.LayerNorm(dim, elementwise_affine=False)
#
# # 打印经过LayerNorm处理后的embedding
# print("y: ", layer_norm(embedding))
#
# # 定义一个小的正数，用于保持数值稳定性
# eps: float = 0.00001
#
# # 计算embedding的均值，沿着最后一个维度（dim=-1）
# mean = torch.mean(embedding[:, :, :], dim=(-1), keepdim=True)
# # 计算embedding的方差
# var = torch.square(embedding[:, :, :] - mean).mean(dim=(-1), keepdim=True)
#
# # 打印均值的形状（主要为了验证）
# print("mean: ", mean.shape)
#
# # 使用上面计算的均值和方差手动进行Layer Normalization，并打印结果
# print("y_custom: ", (embedding[:, :, :] - mean) / torch.sqrt(var + eps))


# import torch
#
# batch_size, seq_size, dim = 2, 3, 4
# embedding = torch.randn(batch_size, seq_size, dim)
#
# layer_norm = torch.nn.LayerNorm([seq_size, dim], elementwise_affine=False)
# print("y: ", layer_norm(embedding))
#
# eps: float = 0.00001
# mean = torch.mean(embedding[:, :, :], dim=(-2, -1), keepdim=True)
# var = torch.square(embedding[:, :, :] - mean).mean(dim=(-2, -1), keepdim=True)
#
# print("mean: ", mean.shape)
# print("y_custom: ", (embedding[:, :, :] - mean) / torch.sqrt(var + eps))

# 作者：Matrix.小泽直树
# 链接：https://www.zhihu.com/question/487766088/answer/2644783144
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import torch

# 定义批次大小、序列长度和维度
batch_size, seq_size, dim = 2, 3, 4

# 生成一个随机的嵌入张量
embedding = torch.randn(batch_size, seq_size, dim)

# 创建LayerNorm层，并指定归一化的维度。这里关闭了可学习的仿射变换（即不使用scale和shift参数）
layer_norm = torch.nn.LayerNorm([seq_size, dim], elementwise_affine=False)
# 对嵌入进行LayerNorm处理并打印结果
print("y: ", layer_norm(embedding))

# 定义一个小的正数值以防止分母为0
eps: float = 0.00001

# 计算嵌入的均值，沿着序列长度和维度方向
mean = torch.mean(embedding[:, :, :], dim=(-2, -1), keepdim=True)
# 计算嵌入的方差
var = torch.square(embedding[:, :, :] - mean).mean(dim=(-2, -1), keepdim=True)

# 打印均值的形状
print("mean: ", mean.shape)

# 使用自定义方法对嵌入进行归一化处理，并打印结果
print("y_custom: ", (embedding[:, :, :] - mean) / torch.sqrt(var + eps))

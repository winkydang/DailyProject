"""
word2vec的训练和使用：
第一步: 获取训练数据
第二步: 训练词向量
第三步: 模型超参数设定
第四步: 模型效果检验
第五步: 模型的保存与重加载
"""

# 训练词向量工具库的安装
# pip install fasttext

import fasttext
# # 词向量的训练保存和加载
# def dm_fasttext_train_save_load():
#     # 1 使用train_unsupervised(无监督训练方法) 训练词向量
#     # mymodel = fasttext.train_unsupervised('./data/fil9')
#     mymodel = fasttext.train_unsupervised('./data/enwik9')
#     print('训练词向量 ok')
#
#     # 2 save_model()保存已经训练好词向量
#     # 注意，该行代码执行耗时很长
#     mymodel.save_model("./data/fil9.bin")
#     print('保存词向量 ok')
#
#     # 3 模型加载
#     mymodel = fasttext.load_model('./data/fil9.bin')
#     print('加载词向量 ok')
#
# dm_fasttext_train_save_load()  # # 词向量的训练保存和加载
# # Read 142M words
# # Number of words:  847816
# # Number of labels: 0
# # Progress: 100.0% words/sec/thread:   35960 lr:  0.000000 avg.loss:  0.462103 ETA:   0h 0m 0s
# # 训练词向量 ok
# # 保存词向量 ok
# # Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.
# # 加载词向量 ok

# # 查看单词对应的词向量
# # 通过get_word_vector方法来获得指定词汇的词向量, 默认词向量训练出来是1个单词100特征
# def dm_fasttext_get_word_vector():
#     mymodel = fasttext.load_model('./data/fil9.bin')
#
#     myvector = mymodel.get_word_vector('the')
#     # print('myvector->', type(myvector), myvector.shape, myvector)
#     # 检查单词向量质量的一种简单方法就是查看其邻近单词, 通过我们主观来判断这些邻近单词是否与目标单词相关来粗略评定模型效果好坏.
#     print(mymodel.get_nearest_neighbors('sports'))
#     print(mymodel.get_nearest_neighbors('music'))
#
# dm_fasttext_get_word_vector()
# # 运行效果如下：
# # myvector-> <class 'numpy.ndarray'> (100,) [ 0.24424708  0.00137101  0.21698399 -0.49521166  0.18774529 -0.07566711
# #  -0.0190789  -0.2844747  -0.32097837  0.45783624 -0.13621055  0.12894459
# #  -0.16283411  0.07820649  0.02786446  0.32978016  0.3313632   0.16699097
# #   0.19603215 -0.06282996  0.2163517   0.5666377   0.48201585  0.92043704
# #  -0.16679855  0.1910879   0.10615995  0.16773917 -0.3547772   0.28187054
# #   0.3841624   0.37174124 -0.3786779  -0.3112236  -0.01165352 -0.00940421
# #   0.03362618  0.23486325 -0.18471953  0.2542925  -0.01377875  0.23376057
# #   0.21997194  0.04723426  0.45355582 -0.41319835  0.16027239  0.12129036
# #  -0.19911546  0.0571361  -0.21997103 -0.22483616 -0.11954155  0.09341775
# #   0.22438177  0.12428756 -0.0920734  -0.25644216  0.23419413 -0.11661622
# #  -0.07692335  0.17385502  0.4645882   0.08675645  0.32713038  0.16862518
# #  -0.05341254 -0.2530159  -0.30873737 -0.0370706   0.08525379  0.39472756
# #  -0.29433262 -0.14586505  0.11277083  0.2520444  -0.1386315   0.01503764
# #   0.5604489  -0.17872281 -0.09159878 -0.15869305  0.25898144 -0.28982612
# #   0.07663415 -0.17539795  0.1765538   0.14150535  0.07469802  0.15940772
# #  -0.22309186 -0.1216913  -0.10152761  0.21562283 -0.0585825   0.01672902
# #  -0.04579772  0.2415914  -0.3510014  -0.26789767]

# # 模型超参数设定
# # 在训练词向量过程中, 我们可以设定很多常用超参数来调节我们的模型效果, 如:
# # 无监督训练模式: 'skipgram' 或者 'cbow', 默认为'skipgram', 在实践中，skipgram模式在利用子词方面比cbow更好.
# # 词嵌入维度dim: 默认为100, 但随着语料库的增大, 词嵌入的维度往往也要更大.
# # 数据循环次数epoch: 默认为5, 但当你的数据集足够大, 可能不需要那么多次.
# # 学习率lr: 默认为0.05, 根据经验, 建议选择[0.01，1]范围内.
# # 使用的线程数thread: 默认为12个线程, 一般建议和你的cpu核数相同.
#
# model = fasttext.train_unsupervised('data/enwik9', "cbow", dim=300, epoch=1, lr=0.1, thread=8)
# model.save_model('./data/test.bin')
# print(model.get_nearest_neighbors('apple'))
# print(model.get_word_vector('the'))

mymodel = fasttext.load_model('./data/test.bin')
print(mymodel.get_nearest_neighbors('apple'))
myvector = mymodel.get_word_vector('the')
print('myvector->', type(myvector), myvector.shape, myvector)

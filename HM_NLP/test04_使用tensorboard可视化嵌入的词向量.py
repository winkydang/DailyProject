import torch
from tensorflow.keras.preprocessing.text import Tokenizer
from torch.utils.tensorboard import SummaryWriter
import jieba
import torch.nn as nn

# 注意：
# fs = tf.io.gfile.get_filesystem(save_path)
# AttributeError: module 'tensorflow._api.v2.io.gfile' has no attribute 'get_filesystem'
# 错误原因分析：
#  1 from tensorboard.compat import tf 使用了tf 如果安装tensorflow，默认会调用它tf的api函数
import tensorflow as tf
import tensorboard as tb
tf.io.gfile = tb.compat.tensorflow_stub.io.gfile


# 实验：nn.Embedding层词向量可视化分析
# 1 对句子分词 word_list
# 2 对句子word2id求my_token_list，对句子文本数值化sentence2id
# 3 创建nn.Embedding层，查看每个token的词向量数据
# 4 创建SummaryWriter对象, 可视化词向量
#   词向量矩阵embd.weight.data 和 词向量单词列表my_token_list添加到SummaryWriter对象中
#   summarywriter.add_embedding(embd.weight.data, my_token_list)
# 5 通过tensorboard观察词向量相似性
# 6 也可通过程序，从nn.Embedding层中根据idx拿词向量

def dm02_nnembeding_show():

    # 1 对句子分词 word_list
    sentence1 = '传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能'
    sentence2 = "我爱自然语言处理"
    sentences = [sentence1, sentence2]

    word_list = []
    for s in sentences:
        word_list.append(jieba.lcut(s))
    # print('word_list--->', word_list)

    # 2 对句子word2id求my_token_list，对句子文本数值化sentence2id
    mytokenizer = Tokenizer()
    mytokenizer.fit_on_texts(word_list)
    # print(mytokenizer.index_word, mytokenizer.word_index)

    # 打印my_token_list
    my_token_list = mytokenizer.index_word.values()
    print('my_token_list-->', my_token_list)

    # 打印文本数值化以后的句子
    sentence2id = mytokenizer.texts_to_sequences(word_list)  # convert a list of texts (sentences) into sequences of numerical IDs.
    print('sentence2id--->', sentence2id, len(sentence2id))

    # 3 创建nn.Embedding层
    embd = nn.Embedding(num_embeddings=len(my_token_list), embedding_dim=8)  # created an embedding layer embd that can be used as a lookup table to get the embeddings for specific tokens. During the training of your NLP model, these embeddings will be updated based on the learning process to capture meaningful representations of the tokens in your dataset.
    # print("embd--->", embd)
    # print('nn.Embedding层词向量矩阵-->', embd.weight.data, embd.weight.data.shape, type(embd.weight.data))

    # 4 创建SummaryWriter对象 词向量矩阵embd.weight.data 和 词向量单词列表my_token_list
    summarywriter = SummaryWriter()  # PyTorch's SummaryWriter from the TensorBoard library, which is a useful tool for visualizing and analyzing training data during the model training process.
    summarywriter.add_embedding(embd.weight.data, my_token_list)
    summarywriter.close()  # This line closes the SummaryWriter once you have finished writing the embeddings and other summary data. It's important to close the writer to ensure that all the data is written and saved correctly.

    # 5 通过tensorboard观察词向量相似性
    # cd 程序的当前目录下执行下面的命令
    # 启动tensorboard服务 tensorboard --logdir=. --host 0.0.0.0
    # 通过浏览器，查看词向量可视化效果 http://127.0.0.1:6006

    print('从nn.Embedding层中根据idx拿词向量')
    # # 6 从nn.Embedding层中根据idx拿词向量
    for idx in range(len(mytokenizer.index_word)):
        tmpvec = embd(torch.tensor(idx))
        print('%4s'%(mytokenizer.index_word[idx+1]), tmpvec.detach().numpy())  # To summarize, tmpvec.detach().numpy() converts a PyTorch tensor tmpvec into a NumPy array, detached from the computation graph.
        # The detach() method is used to create a new tensor that shares the same data as the original tensor but doesn't require gradients to be computed for it. In other words, it creates a copy of the tensor without any connections to the computation graph, which means it won't be part of any future backpropagation computations.
#       # After calling detach(), the code then calls numpy() on the resulting tensor. This converts the PyTorch tensor into a NumPy array. NumPy is a popular library for numerical computing in Python, and converting the tensor to a NumPy array allows you to perform various numerical operations using NumPy's functions and methods.


dm02_nnembeding_show()


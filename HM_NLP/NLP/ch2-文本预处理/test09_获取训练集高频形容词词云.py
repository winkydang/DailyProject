# 使用jieba中的词性标注功能
from itertools import chain

import jieba.posseg as pseg
import pandas as pd
from matplotlib import pyplot as plt
from wordcloud import WordCloud

# 每句话产生形容词列表
def get_a_list(text):
    r = []

    # 使用jieba的词性标注方法切分文本 找到形容词存入到列表中返回
    for g in pseg.lcut(text):
        if g.flag == "a":
            r.append(g.word)
    return r

# 根据词云列表产生词云
def  get_word_cloud(keywords_list):
    # 实例化词云生成器对象
    wordcloud = WordCloud(font_path="/Users/pc/Library/Fonts/NotoSerifSC-ExtraLight.otf", max_words=100, background_color='white')
    # wordcloud = WordCloud(font_path="./SimHei.ttf", max_words=100, background_color='white')
    # 准备数据
    keywords_string = " ".join(keywords_list)
    # 产生词云
    wordcloud.generate(keywords_string)

    # 画图
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()


# 思路分析 训练集正样本词云 训练集负样本词云
# 1 获得训练集上正样本 p_train_data
#   eg: 先使用逻辑==操作检索符合正样本 train_data[train_data['label'] == 1]
# 2 获取正样本的每个句子的形容词 p_a_train_vocab = chain(*map(a,b))
# 3 调用绘制词云函数
def dm_word_cloud():
    # 1 获得训练集上正样本p_train_data
    #   eg: 先使用逻辑==操作检索符合正样本 train_data[train_data['label'] == 1]
    # train_data = pd.read_csv(filepath_or_buffer='./cn_data/train.tsv', sep='\t')
    train_data = pd.read_csv(filepath_or_buffer='../../cn_data/dev.tsv', sep='\t')
    p_train_data = train_data[train_data['label'] == 1 ]['sentence']

    # 2 获取正样本的每个句子的形容词 p_a_train_vocab = chain(*map(a,b))
    p_a_train_vocab = chain(*map(lambda x: get_a_list(x), p_train_data))
    # print(p_a_train_vocab)
    # print(list(p_a_train_vocab))

    # 3 调用绘制词云函数
    get_word_cloud(p_a_train_vocab)


    print('*' * 60 )
    # 训练集负样本词云
    n_train_data = train_data[train_data['label'] == 0 ]['sentence']

    # 2 获取负样本的每个句子的形容词 p_a_train_vocab = chain(*map(a,b))
    n_a_train_vocab = chain(*map(lambda x: get_a_list(x) , n_train_data)  )
    # print(n_a_dev_vocab)
    # print(list(n_a_dev_vocab))

    # 3 调用绘制词云函数
    get_word_cloud(n_a_train_vocab)


dm_word_cloud()

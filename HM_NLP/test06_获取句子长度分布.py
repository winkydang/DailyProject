# 思路分析 : 获取句子长度分布 -绘制句子长度分布-柱状图 句子长度分布-密度曲线图
# 0 什么是句子长度分布：求长度为50的有多少个 长度51的有多少个 长度为52的有多少个
# 1 设置显示风格plt.style.use('fivethirtyeight')
# 2 pd.read_csv(path, sep='\t') 读训练集 验证集数据
# 3 新增数据长度列：train_data['sentence_length'] = list(map(lambda x:len(x) , ...))
# 4-1 绘制数据长度分布图-柱状图 sns.countplot(x='sentence_length', data=train_data)
#  画图展示 plt.xticks([]) plt.show()
# 4-2  绘制数据长度分布图-曲线图 sns.displot(x='sentence_length', data=train_data)
# 画图展示 plt.yticks([]) plt.show()
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def dm_len_sns_countplot_distplot():
    # 1 设置显示风格plt.style.use('fivethirtyeight')
    plt.style.use('fivethirtyeight')

    # 2 pd.read_csv 读训练集 验证集数据
    train_data = pd.read_csv(filepath_or_buffer='./cn_data/train.tsv', sep='\t')
    dev_data = pd.read_csv(filepath_or_buffer='./cn_data/dev.tsv', sep='\t')

    # 3 求数据长度列 然后求数据长度的分布
    train_data['sentence_length'] =  list( map(lambda x: len(x), train_data['sentence']))

    # 4 绘制数据长度分布图-柱状图
    sns.countplot(x='sentence_length', data=train_data)
    # sns.countplot(x=train_data['sentence_length'])
    # plt.xticks([]) # x轴上不要提示信息  隐藏x轴刻度
    # plt.title('sentence_length countplot')
    plt.show()

    # 5 绘制数据长度分布图-曲线图
    sns.displot(x='sentence_length', data=train_data)
    # sns.displot(x=train_data['sentence_length'])
    # plt.yticks([]) # y轴上不要提示信息
    plt.show()

    # 验证集
    # 3 求数据长度列 然后求数据长度的分布
    dev_data['sentence_length'] = list(map(lambda x: len(x), dev_data['sentence']))

    # 4 绘制数据长度分布图-柱状图
    sns.countplot(x='sentence_length', data=dev_data)
    # sns.countplot(x=dev_data['sentence_length'])
    # plt.xticks([])  # x轴上不要提示信息
    # plt.title('sentence_length countplot')
    plt.show()

    # 5 绘制数据长度分布图-曲线图
    sns.displot(x='sentence_length', data=dev_data)
    # sns.displot(x=dev_data['sentence_length'])
    # plt.yticks([])  # y轴上不要提示信息
    plt.show()

dm_len_sns_countplot_distplot()
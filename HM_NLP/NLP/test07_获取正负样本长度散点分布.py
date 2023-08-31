# 获取正负样本长度散点分布，也就是按照x正负样本进行分组 再按照y长度进行散点图
# train_data['sentence_length'] = list(map(lambda x: len(x), train_data['sentence']))
#  sns.stripplot(y='sentence_length', x='label', data=train_data)
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def dm03_sns_stripplot():
    # 1 设置显示风格plt.style.use('fivethirtyeight')
    plt.style.use('fivethirtyeight')

    # 2 pd.read_csv 读训练集 验证集数据
    train_data = pd.read_csv(filepath_or_buffer='../cn_data/train.tsv', sep='\t')
    dev_data = pd.read_csv(filepath_or_buffer='../cn_data/dev.tsv', sep='\t')

    # 3 求数据长度列 然后求数据长度的分布
    train_data['sentence_length'] = list(map(lambda x: len(x), train_data['sentence']))

    # 4 统计正负样本长度散点图 （对train_data数据，按照label进行分组，统计正样本散点图）
    sns.stripplot(y='sentence_length', x='label', data=train_data)
    plt.show()

    dev_data['sentence_length'] = list(map(lambda x: len(x), dev_data['sentence']))
    sns.stripplot(y='sentence_length', x='label', data=dev_data)
    plt.show()

dm03_sns_stripplot()
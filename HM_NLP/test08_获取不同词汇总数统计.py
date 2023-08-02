# 导入jieba用于分词
# 导入chain方法用于扁平化列表
import jieba
from itertools import chain
import pandas as pd

# pd.read_csv 读训练集 验证集数据
train_data = pd.read_csv(filepath_or_buffer='./cn_data/train.tsv', sep='\t')
dev_data = pd.read_csv(filepath_or_buffer='./cn_data/dev.tsv', sep='\t')

# 进行训练集的句子进行分词, 并统计出不同词汇的总数
train_vocab = set(chain(*map(lambda x: jieba.lcut(x), train_data["sentence"])))
print("训练集共包含不同词汇总数为：", len(train_vocab))

# 进行验证集的句子进行分词, 并统计出不同词汇的总数
valid_vocab = set(chain(*map(lambda x: jieba.lcut(x), dev_data["sentence"])))
print("训练集共包含不同词汇总数为：", len(valid_vocab))

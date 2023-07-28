# 导入必备工具包
import matplotlib
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# 思路分析 : 获取标签数量分布
# 0 什么标签数量分布：求标签0有多少个 标签1有多少个 标签2有多少个
# 1 设置显示风格plt.style.use('fivethirtyeight')
# 2 pd.read_csv(path, sep='\t') 读训练集 验证集数据
# 3 sns.countplot() 统计label标签的0、1分组数量
# 4 画图展示 plt.title() plt.show()
# 注意1：sns.countplot()相当于select * from tab1 group by
def dm_label_sns_countplot():
    # 1 设置显示风格plt.style.use('fivethirtyeight')
    # plt.style.use('fivethirtyeight')
    sns.set_style("whitegrid")

    # Update font properties for displaying Chinese characters
    font = {'family': 'Arial Unicode MS', 'size': 12}  # or 'Microsoft YaHei'
    # Set the font properties as default for all text elements
    plt.rc('font', **font)

    # 2 pd.read_csv 读训练集 验证集数据  返回类型是DataFrame类型
    train_data = pd.read_csv(filepath_or_buffer='./cn_data/train.tsv', sep='\t')
    dev_data = pd.read_csv(filepath_or_buffer='./cn_data/dev.tsv', sep='\t')

    # 3 sns.countplot() 统计label标签的0、1分组数量
    sns.countplot(x='label', data=train_data)  # using the Seaborn library in Python to create a count plot based on the data in the train_data DataFrame.

    # 4 画图展示 plt.title() plt.show()
    # Add labels and title to the plot
    # font = FontProperties(fname=r'/Users/pc/Library/Fonts/NotoSerifSC-ExtraLight.otf', size=12)
    # plt.xlabel('标签', fontproperties=font)  # 使用自己下载的字体
    # plt.ylabel('总和', fontproperties=font)
    plt.xlabel('标签')
    plt.ylabel('总和')
    plt.title('train_label')
    plt.show()

    # 验证集上标签的数量分布
    # 3-2 sns.countplot() 统计label标签的0、1分组数量
    sns.countplot(x='label', data=dev_data)

    # 4-2 画图展示 plt.title() plt.show()
    plt.title('dev_label')
    plt.show()

dm_label_sns_countplot()


import jieba
# 导入keras中的词汇映射器Tokenizer
from tensorflow.keras.preprocessing.text import Tokenizer
# 导入用于对象保存与加载的joblib
# from sklearn.externals import joblib
import joblib

# onehot编码实现
# 思路分析 生成onehot
# 1 准备语料 vocabs
# 2 实例化词汇映射器Tokenizer, 使用映射器拟合现有文本数据 (内部生成 index_word word_index)
# 2-1 注意idx序号-1
# 3 查询单词idx 赋值 zero_list，生成onehot
# 4 使用joblib工具保存映射器 joblib.dump()
def dm_onehot_gen():

    # 1 准备语料 vocabs
    vocabs = {"周杰伦", "陈奕迅", "王力宏", "李宗盛", "吴亦凡", "鹿晗"}  # 集合类型

    # 2 实例化词汇映射器Tokenizer, 使用映射器拟合现有文本数据 (内部生成 index_word word_index)
    # 2-1 注意idx序号-1
    mytokenizer = Tokenizer()
    mytokenizer.fit_on_texts(vocabs)

    # 3 查询单词idx 赋值 zero_list，生成onehot
    for vocab in vocabs:
        zero_list = [0] * len(vocabs)
        idx = mytokenizer.word_index[vocab] - 1
        zero_list[idx] = 1
        print(vocab, '的onehot编码是', zero_list)

    # 4 使用joblib工具保存映射器 joblib.dump()
    mypath = './mytokenizer'
    joblib.dump(mytokenizer, mypath)
    print('保存mytokenizer End')

    # 注意5-1 字典没有顺序 onehot编码没有顺序 []-有序 {}-无序 区别
    # 注意5-2 字典有的单词才有idx idx从1开始
    # 注意5-3 查询没有注册的词会有异常 eg: 狗蛋  mytokenizer.word_index['狗蛋']   提示：{KeyError}'狗蛋'
    print(mytokenizer.word_index)
    print(mytokenizer.index_word)

dm_onehot_gen()


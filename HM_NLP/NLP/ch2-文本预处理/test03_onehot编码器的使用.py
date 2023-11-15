# 思路分析
# 1 加载已保存的词汇映射器Tokenizer joblib.load(mypath)
# 2 查询单词idx 赋值zero_list，生成onehot 以token为'李宗盛'
# 3 token = "狗蛋" 会出现异常
import joblib


def dm_onehot_use():

    vocabs = {"周杰伦", "陈奕迅", "王力宏", "李宗盛", "吴亦凡", "鹿晗"}

    # 1 加载已保存的词汇映射器Tokenizer joblib.load(mypath)
    mypath = './mytokenizer'
    mytokenizer = joblib.load(mypath)

    # 2 编码token为"李宗盛"  查询单词idx 赋值 zero_list，生成onehot
    token = "李宗盛"
    zero_list = [0] * len(vocabs)
    idx = mytokenizer.word_index[token] - 1
    zero_list[idx] = 1
    print(token, '的onehot编码是', zero_list)

dm_onehot_use()
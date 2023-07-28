# import jieba
# content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
# # 精确模式：试图将句子最精确地切开，适合文本分析。也属于默认模式
# t1 = jieba.cut(content, cut_all=False)  # cut_all默认为False
# print(t1)
# # # 将返回一个生成器对象
# # <generator object Tokenizer.cut at 0x7f8d9053e650>
#
# # 若需直接返回列表内容, 使用jieba.lcut即可
# t2 = jieba.lcut(content, cut_all=False)
# print(t2)
# # ['传智', '教育', '是', '一家', '上市公司', '，', '旗下', '有', '黑马', '程序员', '品牌', '。', '我', '是', '在', '黑马', '这里', '学习', '人工智能']

# # 全模式分词，把句子中所有的可以成词的词语都扫描出来，速度非常快但不能消除歧义。
# import jieba
# content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
# # 若需直接返回列表内容, 使用jieba.lcut即可
# t3 = jieba.lcut(content, cut_all=True)
# print(t3)
# # ['传', '智', '教育', '是', '一家', '上市', '上市公司', '公司', '，', '旗下', '下有', '黑马', '程序', '程序员', '品牌', '。', '我', '是', '在', '黑马', '这里', '学习', '人工', '人工智能', '智能']
# # 注意1：人工智能全模型分成三个词
# # 注意2：逗号和句号也给分成了词

# # 搜索引擎模式分词: 在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。
# import jieba
# content = "传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能"
# jieba.cut_for_search(content)
#
# # # 将返回一个生成器对象
# # <generator object Tokenizer.cut_for_search at 0x7f8d90e5a550>
#
# # 若需直接返回列表内容, 使用jieba.lcut_for_search即可
# t4 = jieba.lcut_for_search(content)
# print(t4)
# # ['传智', '教育', '是', '一家', '上市', '公司', '上市公司', '，', '旗下', '有', '黑马', '程序', '程序员', '品牌', '。', '我', '是', '在', '黑马', '这里', '学习', '人工', '智能', '人工智能']
# # 对'上市公司'等较长词汇都进行了再次分词.

# # 中文繁体分词。针对中国香港, 台湾地区的繁体文本进行分词。
# import jieba
# content = "煩惱即是菩提，我暫且不提"
# print(jieba.lcut(content))
# # ['煩惱', '即', '是', '菩提', '，', '我', '暫且', '不', '提']

# # 使用用户自定义词典
# import jieba
# sentence = '传智教育是一家上市公司，旗下有黑马程序员品牌。我是在黑马这里学习人工智能'
# # 1 没有使用用户自定义词典
# mydata = jieba.lcut(sentence, cut_all=False)
# print('mydata-->', mydata)
#
# # 2 使用用户自定义词典
# jieba.load_userdict("./userdict.txt")
# mydata2 = jieba.lcut(sentence, cut_all=False)
# print('mydata2-->', mydata2)
#
# # 没有使用用户自定义词典的分词效果
# # mydata--> ['传智', '教育', '是', '一家', '上市公司', '，', '旗下', '有', '黑马', '程序员', '品牌', '。', '我', '是', '在', '黑马', '这里', '学习', '人工智能']
#
# # 使用用户自定义词典的分词效果
# # mydata2--> ['传智教育', '是', '一家', '上市公司', '，', '旗下', '有', '黑马程序员', '品牌', '。', '我', '是', '在', '黑马', '这里', '学习', '人工智能']

# # POS 词性标注
# import jieba.posseg as pseg
# print(pseg.lcut("我爱北京天安门"))
# # [pair('我', 'r'), pair('爱', 'v'), pair('北京', 'ns'), pair('天安门', 'ns')]
# # 结果返回一个装有pair元组的列表, 每个pair元组中分别是词汇及其对应的词性, 具体词性含义请参照[附录: jieba词性对照表]()











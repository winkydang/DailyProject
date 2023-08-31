# 一般n-gram中的n取2或者3, 这里取2为例
ngram_range = 3

def create_ngram_set(input_list):
    """
    description: 从数值列表中提取所有的n-gram特征
    :param input_list: 输入的数值列表, 可以看作是词汇映射后的列表,
                       里面每个数字的取值范围为[1, 25000]
    :return: n-gram特征组成的集合

    eg:
    # >>> create_ngram_set([1, 3, 2, 1, 5, 3])
    {(3, 2), (1, 3), (2, 1), (1, 5), (5, 3)}
    """
    # t1 = [input_list[i:] for i in range(ngram_range)]
    t1 = []
    for i in range(ngram_range):
        t1.append(input_list[i:])
    t2 = zip(*t1)
    return set(t2)
    # return set(zip(*[input_list[i:] for i in range(ngram_range)]))


input_list = [1, 3, 2, 1, 5, 3]
res = create_ngram_set(input_list)
print(res)



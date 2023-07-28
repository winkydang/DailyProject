# --coding:utf-8--

import re
import jieba
import jieba.analyse
import numpy as np
import jieba.posseg as pseg
import common

kwDic = {'1': ['票面利率', '发行结果', '解*押', '文件', '募集说明书', '申购', '清算', '信用评级', '回复', '进展', '独立意见', '名单', '报告', '说明', '发行', '停牌', '签署协议', '完成', '决议', '质押', '质押', '解*冻', '更名', '提示性', '票据', '会议', '通知', '申报', '发行结果'], '2': ['董事', '监视', '股东', '秘书', '子公司', '高管'], '3': ['A级', 'B级', 'C级', 'A类', 'B类', 'C类', '优先A', '优先B', '优先级', '次级']}
print(kwDic)



def string_hash(source, hashbits=64):
    if source == "":
        return 0
    else:
        x = ord(source[0]) << 7
        # print(x)
        m = 1000003
        mask = 2 ** hashbits - 1
        for c in source:
            x = ((x * m) ^ ord(c)) & mask
        x ^= len(source)
        if x == -1:
            x = -2
        x = bin(x).replace('0b', '').zfill(64)[-64:]
        # print(source, x)
        return str(x)

def simhash(content):
    if content == None:
        return '00'
    seg = jieba.cut(content)
    keyWord = jieba.analyse.extract_tags(' '.join(seg), topK=30, withWeight=True, allowPOS=())
    # print(keyWord)
    keyList = []
    # print('Segment words and weight:', keyWord)
    for feature, weight in keyWord:
        # print(feature, weight)
        weight = int(weight * 20)
        feature = string_hash(feature)
        # print(feature, weight)
        temp = []
        for i in feature:
            if (i == '1'):
                temp.append(weight)
            else:
                temp.append(-weight)
                # print(temp)
        keyList.append(temp)
    list1 = np.sum(np.array(keyList), axis=0)
    if (keyList == []):  # 编码读不出来
        return '00'
    simhash = ''
    for i in list1:
        if (i > 0):
            simhash = simhash + '1'
        else:
            simhash = simhash + '0'
    return simhash

def hammingDis(hash1, hash2):

    t1 = '0b' + hash1
    t2 = '0b' + hash2
    n = int(t1, 2) ^ int(t2, 2)
    i = 0
    while n:
        n &= (n - 1)
        i += 1
    return i

def hashDis(hash1, hash2):
    n = 0.0
    if len(hash1) == len(hash2):
        for i in range(len(hash1)):
            if hash1[i] == hash2[i]:
                n = n + 1.0
        rst = n / len(hash1)
    else:
        rst = 0.0
    return rst

def similarValue(content1, content2):
    simhs1 = simhash(content1)
    # print('#'* 10)
    simhs2 = simhash(content2)
    # return hammingDis(simhs1, simhs2)
    rst = hashDis(simhs1, simhs2)
    # print(simhs1)
    # print(simhs2)
    # print(rst)
    return rst

def similarTitle(title1, title2):

    if '关于' in title1 and '关于' in title2:
        title1 = title1.split('关于')[-1]
        title2 = title2.split('关于')[-1]

    if '】' in title1 and '【' in title1:
        t1tmp = (title1.split('【')[1]).split('】')[0]
        if len(t1tmp) < 6:
            title1 = title1.split('】')[-1]
        else:
            title1 = t1tmp
    if '】' in title2 and '【' in title2:
        t2tmp = (title2.split('【')[1]).split('】')[0]
        if len(t2tmp) < 6:
            title2 = title2.split('】')[-1]
        else:
            title2 = t2tmp

    rst = set(title1).difference(set(title2))
    if float(len(rst)/(len(title1)+len(title2))) < 0.1:
        return 1.0

    # print(title1)
    # print(title2)
    t1kw = re.findall(r"(\d+\.\d+%|\d+\.\d+万|\d+\.\d+亿|\d+%|\d*万|\d*亿)", title1)
    # print(t1kw)

    if len(t1kw) >= 1:
        if t1kw[-1] in title2 and len(t1kw[-1]) >1:
            return 1.0

    w1flag = []

    words1 = pseg.cut(title1)
    words2 = pseg.cut(title2)

    for w1, f1 in words1:
        if f1 not in 'x':
            w1flag.append(f1)
    for w2, f2 in words2:
        if f2 not in 'x':
            w1flag.append(f2)

    w1flag = set(w1flag)
    # print('w1flag', w1flag)

    wordflagDic = {}
    sorce = 0.0
    sorce1 = 0.0
    sorce2 = 0.0
    for fi in w1flag:

        l1 = 0
        l2 = 0

        # print('fi:', fi)
        words1 = pseg.cut(title1)
        words2 = pseg.cut(title2)

        w1word = []
        w2word = []
        for w1, f1 in words1:
            l1 = l1 + 1

            # print(len(w1), len(fi))
            # print(str(f1) == str(fi))
            if str(f1) == str(fi):
                # print('f1:', f1, fi)
                # print('w1:', w1)
                # print(w1)
                w1word.append(w1)

        for w2, f2 in words2:
            l2 = l2 + 1

            # print(len(w2), len(fi))
            # print(str(f2) == str(fi))
            if str(f2) == str(fi):
                # print('f2:', f2, fi)
                # print('w2:', w2)
                w2word.append(w2)

        # print('!!!!!!', w1word, w2word)


        # print('defference11', list(set(w2word).difference(set(w1word))))
        wordflagDic[fi] = list(set(w2word).difference(set(w1word))) + list(set(w1word).difference(set(w2word)))
        # print('defference12', len(list(set(w2word).difference(set(w1word))))/(len(list(set(w2word)))+len(list(set(w1word)))), len(list(set(w2word))), len(list(set(w2word).difference(set(w1word)))))
        sorce1 = sorce1 + len(list(set(w2word).difference(set(w1word))))/(len(list(set(w2word)))+len(list(set(w1word))))
        # print('defference21', list(set(w1word).difference(set(w2word))))
        # print('defference22', len(list(set(w1word).difference(set(w2word)))) / (len(list(set(w1word)))+len(list(set(w2word)))), len(list(set(w1word))), len(list(set(w1word).difference(set(w2word)))))
        sorce2 = sorce2 + len(list(set(w1word).difference(set(w2word)))) / (len(list(set(w1word)))+len(list(set(w2word))))

    # print(wordflagDic, len(wordflagDic))
    if 'm' in wordflagDic.keys():
        if len(wordflagDic['m']) != 0:
            return 0.0


    if 'ns' in wordflagDic.keys():

        if len(wordflagDic['ns']) != 0:
            return 0.0

    if similarValue(title1, title2) > 0.95 or (sorce1 == 0.0 and sorce2 == 0.0):
        # print('sorce:1')
        return 1.0
    else:
        sorce = 1 - (sorce1 + sorce2)
        # print('sorce:', sorce)
        return sorce


def includeTitle(title1, title2):
    titleC1 = jieba.lcut(title1.replace('\n', '').replace(' ', ''))
    titleC2 = jieba.lcut(title2.replace('\n', '').replace(' ', ''))

    n = 0
    m = 0
    souce = -1
    for ti in titleC1:
        # print(ti)
        if ti in title2:
            # print(ti, title2)
            n = n + 1
    # print(n, len(titleC1))
    if n == len(titleC1):
        souce = 1
    for ti in titleC2:
        # print(ti)
        if ti in title1:
            # print(ti, title1)
            m = m + 1
    # print(m, len(titleC2))
    if m == len(titleC2):
        souce = 1

    # print(souce)
    return souce

def main(obj2, title1, title2, content1, content2):
    title1 = common.removePunctuation(title1)
    title2 = common.removePunctuation(title2)
    #print(title1)
    #print(title2)
    s1 = includeTitle(title1, title2)
    # print('s1', s1)
    if s1 == -1:
        s2 = similarTitle(title1, title2)
        # print('s2', s2)
        c = similarValue(content1, content2)
        # print('c', c)
        if s2 < 0.4 or (s2 < 0.55 and c < 0.85):
            return ''
        else:
            return obj2
    else:
        return obj2



if __name__ == '__main__':
    print(main(33333, '中关村发展集团董事长赵长山被调查', '2023中关村发展集团党委书记、董事长赵长山：共管理母子基金37只，总规模317亿元', '1991', '4'))

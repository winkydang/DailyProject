import jieba
import hashlib


class Simhash(object):
    def __init__(self, tokens='', hashbits=64):
        self.hashbits = hashbits
        self.hash = self.simhash(tokens)

    def __str__(self):
        return str(self.hash)

    def __hash__(self):
        return self.hash

    def simhash(self, tokens):
        v = [0] * self.hashbits
        for t in [self._string_hash(x) for x in tokens]:
            for i in range(self.hashbits):
                bitmask = 1 << i
                if t & bitmask:
                    v[i] += 1
                else:
                    v[i] -= 1
        fingerprint = 0
        for i in range(self.hashbits):
            if v[i] >= 0:
                fingerprint += 1 << i
        return fingerprint

    def _string_hash(self, string):
        if string == "":
            return 0
        else:
            x = hashlib.md5(string.encode('utf-8')).hexdigest()
            return int(x, 16)


def tokenize(text):
    """
    对文本进行分词
    """
    seg_list = jieba.cut(text)
    tokens = []
    for seg in seg_list:
        seg = seg.strip()
        if seg:
            tokens.append(seg)
    return tokens


def is_duplicate(title, title_hashes, threshold):
    """
    判断标题是否重复
    """
    tokens = tokenize(title)
    sh = Simhash(tokens)
    for h in title_hashes:
        d = sh.distance(h)
        if d < threshold:
            return True
    return False


# 示例用法
titles = ["今日头条", "今天的头条新闻", "今天的新闻头条", "明日头条"]
title_hashes = []
threshold = 3  # 设置哈希距离阈值
for title in titles:
    if not is_duplicate(title, title_hashes, threshold):
        title_hashes.append(Simhash(tokenize(title)))
        print(title)

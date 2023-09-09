class Solution:
    def reverseWords(self, s: str) -> str:
        # 先反转整个字符串
        s = s[::-1]
        # 再反转每个单词
        # tmp = s.split(' ')
        tmp = s.split()
        tmp = [i for i in tmp if i]
        res = []
        for i in tmp:
            i.strip()
            i = i[::-1]
            res.append(i)
        return ' ' .join(res).strip()

        # # 方式二
        # tmp = s.split()  # ['a', 'good', 'example']
        # tmp = tmp[::-1]
        # return ' '.join(tmp)
        # # 方式三
        # # return ' '.join(s.split()[::-1])


cls = Solution()
s = "a good   example"
res = cls.reverseWords(s)
print(res)

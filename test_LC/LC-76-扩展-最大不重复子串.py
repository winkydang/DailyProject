def longest_unique_substring(s):
    if not s:
        return ""

    char_set = set()  # 用于存储已遍历过的字符的集合，以检测重复字符
    start = 0  # 跟踪不重复子串的起始位置
    max_length = 0  # 最长不重复子串的长度
    max_substring = ""  # 存储最长不重复子串

    for end in range(len(s)):  # 遍历字符串s
        while s[end] in char_set:
            char_set.remove(s[start])  # 一直移除char_set中的字符，直到s[end]不在char_set中，进行下一次最长子串的寻找
            start += 1

        char_set.add(s[end])  # 遇到一个新字符，添加到char_set
        current_length = end - start + 1  # 计算当前不重复子串的长度

        if current_length > max_length:
            max_length = current_length
            max_substring = s[start:end + 1]

    return max_substring


# 示例
# input_str = "abcabcbb"  # abc
input_str = "abcabcggghhhhhhhhbb"  # abcg
# input_str = "abcahhgb"  # bcah
result = longest_unique_substring(input_str)
print(result)


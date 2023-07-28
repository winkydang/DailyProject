def edit_distance(s1, s2):
    """
    计算两个字符串之间的编辑距离
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

def lcs(s1, s2):
    """
    计算两个字符串之间的最长公共子序列
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def is_duplicate(title, titles, threshold):
    """
    判断标题是否重复
    """
    for t in titles:
        ed = edit_distance(title, t)
        lcs_len = lcs(title, t)
        similarity = lcs_len / max(len(title), len(t))
        if ed < threshold or similarity > threshold:
            return True
    return False

# 示例用法
titles = ["今日头条", "今天的头条新闻", "今天的新闻头条", "明日头条"]
unique_titles = []
threshold = 0.6  # 设置相似度阈值
for title in titles:
    if not is_duplicate(title, unique_titles, threshold):
        unique_titles.append(title)
print(unique_titles)  # 输出：['今日头条', '今天的头条新闻']

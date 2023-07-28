import pandas as pd

dict0 = {'d': 1, 'B': 2, 'C': 3}

df_1 = pd.DataFrame(dict0, index=[0])
print(df_1)
print('---------------------------')

# 多个字典数据
dict1 = {'A': 1, 'B': 2, 'C': 3}
dict2 = {'A': 4, 'B': 5, 'C': 6}
dict3 = {'A': 7, 'B': 8, 'C': 9}

# 构建字典列表
dict_list = [dict1, dict2, dict3]

# 转存为DataFrame
# df = pd.DataFrame(dict_list)

# df_1 = df_1.append(pd.DataFrame(dict1, index=[0]))
df_1 = df_1.append(dict_list)
# df_1 = pd.concat(df_1, df)
print(df_1)
print('---------------------------')


# 打印DataFrame
# print(df)

# import pandas as pd
#
# # 假设你有两个Series数据，如下所示：
# # Series 1
# # 编号  bool值
# # 1    True
# # 2    False
# # 3    True
#
# # Series 2
# # 编号  bool值
# # 1    True
# # 2    True
# # 3    False
#
# # 创建DataFrame
# df1 = pd.DataFrame({'编号': [1, 2, 3], 'bool值': [True, False, True]})
# df2 = pd.DataFrame({'编号': [1, 2, 3], 'bool值': [True, True, False]})
#
# # 合并DataFrame
# merged_df = pd.merge(df1, df2, on='编号', suffixes=('_1', '_2'))
#
# # 筛选出两个bool值均为True的行
# result_df = merged_df[(merged_df['bool值_1'] == True) & (merged_df['bool值_2'] == True)]
#
# # 获取满足条件的编号
# matching_ids = result_df['编号'].tolist()
#
# print(matching_ids)

# print(True and False)  # False
# print(True or False)  # True

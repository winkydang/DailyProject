# import pandas as pd
# import re
#
#
# data = pd.read_excel('./123123.xlsx')
#
# # print(data['证券代码'])
#
# output = pd.DataFrame(columns=data.columns)
# # output = pd.DataFrame()
# # output_index = 0
#
# for index in range(len(data)):
#     temp = data.loc[index, '证券代码']
#     if not re.search('^\d{6,9}(\.[A-Z]{,2})?$', temp):
#         # print(temp)
#         # output.append({data.columns[0]:data.loc[index, data.columns[0]],data.columns[1]:data.loc[index, data.columns[1]],data.columns[2]:data.loc[index, data.columns[2]],data.columns[3]:data.loc[index, data.columns[3]]})
#         # output.append()不是inplace修改，会生成一个新的df
#         output = output.append({data.columns[0]:data.loc[index, data.columns[0]],data.columns[1]:data.loc[index, data.columns[1]],data.columns[2]:data.loc[index, data.columns[2]],data.columns[3]:data.loc[index, data.columns[3]]}, ignore_index = True)
#         # output_index += 1
# print(output)
#
# writer = pd.ExcelWriter('../../out_file/result.xlsx')
# output.to_excel(writer, sheet_name='1')
# writer.close()

# from test_AI.test_0526_openaiAPI import llm
# print(llm)

# from test1.aaa.a import a123
# print(a123)

# from test111.aaa.a import a123
# print(a123)


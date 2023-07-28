import datetime

print(datetime.datetime.today())  # 2023-07-26 14:03:26.497409

# import re
#
# pattern = r"\."  # 匹配句号
# text = "The price is $10.99."
# match = re.search(pattern, text)
# if match:
#     print(match)  # <re.Match object; span=(16, 17), match='.'>
#     print(re.match(pattern, text))  # None
#     print(re.search(pattern, text))  # <re.Match object; span=(16, 17), match='.'>
#     print(re.findall(pattern, text))  # ['.', '.']
#     print(re.split(pattern, text))  # ['The price is $10', '99', '']
#     print(re.sub(pattern, '~', text))  # The price is $10~99~
#     print("找到句号")
# else:
#     print("未找到句号")

# import re
#
# input_str = "My phone number is 123-456-7890 and my friend's number is 987-654-3210."
#
# # 定义匹配电话号码的正则表达式
# pattern = r'\d{3}-\d{3}-\d{4}'
#
# # 使用正则表达式进行替换
# replacement = "XXX-XXX-XXXX"
# result = re.sub(pattern, replacement, input_str)
#
# print(result)

# import re
#
# input_str2 = "*****买入3L*****"
#
# # pattern3 = r'\d{1}L'    # re.findall(pattern3, input_str2)，匹配到 ['3']
# # 定义匹配数字加'L'的正则表达式
# pattern2 = r'(\d+)L'  # re.findall(pattern2, input_str2)，匹配到 ['3L']
#
# # 使用正则表达式进行替换
# replacement2 = r"\1厘"  # \1表示匹配到的第一个分组，即数字部分。保留数字3，以防数字3被替换掉
# result2 = re.sub(pattern2, replacement2, input_str2)
# print(result2)  # *****买入3厘*****
#
# print(re.match(pattern2, input_str2))
# print(re.search(pattern2, input_str2))
# print(re.findall(pattern2, input_str2))  # ['3']
#
# pattern3 = r'\d{1}L'
# print(re.match(pattern3, input_str2))
# # print(re.search(pattern3, input_str2))
# # print(re.findall(pattern3, input_str2))  # ['3L']

# import os
#
# import pandas as pd
#
# from settings import cur_path
#
# file_path = os.path.join(cur_path, 'file/title_emo.csv')
# df = pd.read_csv(file_path)
# print(df)
#
# import time
#
# now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# print(now_date)

# import oracledb
# import os
#
# un = os.environ.get('PYTHON_USERNAME')
# pw = os.environ.get('PYTHON_PASSWORD')
# cs = os.environ.get('PYTHON_CONNECTSTRING')
#
# with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
#     with connection.cursor() as cursor:
#         sql = """select sysdate from dual"""
#         for r in cursor.execute(sql):
#             print(r)


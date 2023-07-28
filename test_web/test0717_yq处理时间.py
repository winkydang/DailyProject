import os
import pandas as pd
from settings import cur_path

wind_path = os.path.join(cur_path, 'test_web/file/wind债券公告2023-07-17 09.32.xlsx')
df_wind = pd.read_excel(wind_path, sheet_name=0, engine='openpyxl')
df_local = pd.read_excel(os.path.join(cur_path, 'test_web/file/0714-0716入库公告数据.xlsx'), sheet_name=0, engine='openpyxl')

data = {
    '公告标题': df_wind['公告标题'],
    'wind_发布时间': df_wind['发布时间']
}
df_tar = pd.DataFrame(data)

# 添加一个新列，使用空的Series对象进行初始化
df_wind['本地入库时间'] = pd.Series

for index_1, row_1 in df_wind.iterrows():
    for index_2, row_2 in df_local.iterrows():
        t1 = row_1['公告标题'].replace('：', ':').replace('（', '(').replace('）', ')').replace(' ', '')
        t2 = row_2['title'].replace('：', ':').replace('（', '(').replace('）', ')').replace(' ', '')
        if t1 == t2:
            df_wind.loc[index_1, '本地入库时间'] = row_2['createTime']
            break
        else:
            df_wind.loc[index_1, '本地入库时间'] = None
save_path = os.path.join(cur_path, 'test_web/file/save.xlsx')
df_wind.to_excel(save_path)

print()
# '亚药转债:关于向下修正可转换公司债券转股价格的公告'
# '亚太药业：关于向下修正可转换公司债券转股价格的公告'
# ':：'


# '公告及通告 - [薪酬委员会的职权范围]'

'益丰药房:关于回复上海证券交易所《关于益丰大药房连锁股份有限公司向不特定对象发行可转换公司债券的审核中心意见落实函》的公告'
'关于回复上海证券交易所《关于益丰大药房连锁股份有限公司向不特定对象发行可转换公司债券的审核中心意见落实函》的公告'
'关于益丰大药房连锁股份有限公司向不特定对象发行可转换公司债券的审核中心意见落实函的回复报告'
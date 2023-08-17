import datetime
import os
import pandas as pd
import pymysql
from settings import cur_path
from test1 import conf


def addSql(sql):
    print(sql)
    db_link = pymysql.connect(host=conf.linkserver, user=conf.linkusername, password=conf.linkpassword,
                              database=conf.linkname, charset='utf8')
    log = "begin to connect database %s,user:%s,password:%s,database name:%s" % (conf.linkserver, conf.linkusername, conf.linkpassword, conf.linkname)
    print(log)

    link_cursor = db_link.cursor()

    try:
        link_cursor.execute(sql)
        db_link.commit()  # 提交到数据库执行，一定要记提交哦
    except Exception as e:
        db_link.rollback()  # 发生错误时回滚
        print(e)
    link_cursor.close()
    db_link.close()


def makeSql(dic, table):
    sqlList = []
    for key in dic.keys():
        string = "{} = '{}'".format(key, dic[key])
        sqlList.append(string)
    sqlContent = ','.join(sqlList)

    sql = "insert into " + table + " SET {}".format(sqlContent)
    addSql(sql)


if __name__ == '__main__':
    path = os.path.join(cur_path, 'test1/file/舆情_1831.xlsx')
    df_1 = pd.read_excel(path).fillna('')

    for index, value in enumerate(df_1.values):
        rowdic = {}
        rowdic['ITEM'] = int(value[3])
        rowdic['KEYWORDS'] = value[7]
        rowdic['CATEGORY'] = value[2]
        rowdic['NOT_KEYWORDS'] = value[8]
        rowdic['WEIGHT'] = value[9]
        rowdic['CREATETIME'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        rowdic['UPDATETIME'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        rowdic['FIRST_LEVEL'] = value[0]
        rowdic['SEC_LEVEL'] = value[1]
        rowdic['EMO'] = int(value[6]) if value[6] != '' else ''
        rowdic['IMPORTANCE'] = value[5]
        rowdic['ZUIYOU'] = int(value[10]) if value[10] != '' else ''
        rowdic['FLAG'] = value[4]

        makeSql(rowdic, 't_dc_keywords_category_classify_bak20230807')
        # pass



# INSERT INTO `linkdata`.`t_dc_keywords_category_classify_bak20230808` (`OBJID`, `KEYWORDS`, `CATEGORY`, `NOT_KEYWORDS`, `CREATETIME`, `UPDATETIME`, `FIRST_LEVEL`, `SEC_LEVEL`, `WEIGHT`, `ITEM`, `EMO`, `IMPORTANCE`, `ZUIYOU`, `FLAG`) VALUES (2, '困局,停产,停工,减产,停业,停飞,关店,过度依赖;业务*[停滞,停顿];\r\n[暂停,停止]*[运营,业务,运行,合作,生产];经营*[异常,困难,不确定性,影响];\r\n[运营,业务,运行,合作,生产]*[暂停,停止];[异常,困难,不确定性,影响]*经营;\r\n关店;销售*疲软;产量*受限;订单减少,中断合作,盲目扩张,主业不突出;暴露*短板;\r\n产能*[稀缺,不足];供应*吃紧;撤销*营业部;出货*下滑;[停运,停用]*风波;\r\n原材料*价格*涨;管理乱象,危机迷局;客运量*降;[出售,剥离]*业务;业务*[出售,剥离];\r\n投诉量*[居首,增长];[停贷,断贷]*事件;重大损失；', '经营问题', NULL, '2021-05-07 15:18:21', '2023-02-20 14:52:30', '企业经营', '生产经营', '经营情况;其他经营情况;', '13', '-1', '高', NULL, '预警项');
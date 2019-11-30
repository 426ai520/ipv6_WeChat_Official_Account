# _*_ coding:utf-8 _*_
# 用于根据输入查询数据库内容并返回查询结果
import pymysql

def db_connect():
    connect = pymysql.Connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="12345",
        db="v6_db",
        charset='utf8'
    )
    return connect

def db_close():
    db_connect().commit()
    db_connect().close()

def reply_result(rec_text):
    cursor = db_connect().cursor()
    if rec_text == '1':
        sql = "SELECT sum_people FROM bath_tbl WHERE time=(SELECT MAX(time) FROM bath_tbl)"
        cursor.execute(sql)
        number = cursor.fetchall()
        for n in number:
            rep_text = '浴室当前使用人数为：' + str(n[0]) + '\n' + '浴室空闲位置为：' + str(30-n[0])
            return rep_text
    elif rec_text == '2':
        sql = "SELECT sum_people FROM water_tbl WHERE time=(SELECT MAX(time) FROM water_tbl)"
        cursor.execute(sql)
        number = cursor.fetchall()
        for n in number:
            rep_text = '水房当前排队人数为：' + str(n[0]) + '\n' + '水房空闲位置为：' + str(30-n[0])
            return rep_text
    else:
        return rec_text
    db_close()



# _*_ coding:utf-8 _*_
# 主动查询数据库
import pymysql
import time

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

def db_select():
    cursor = db_connect().cursor()
    sql = "SELECT sum_people FROM bath_tbl WHERE time=(SELECT MAX(time) FROM bath_tbl)"
    cursor.execute(sql)
    number = cursor.fetchall()
    for n in number:
        return n[0]
    db_close()

def active_send():
    n = db_select()
    print('上一次', n)
    while True:
        m = db_select()
        print('本次', m)
        time.sleep(10)
        if m != n:
            n = m
            return "当前人数为" + str(n)

if __name__ == '__main__':
    while True:
        print(active_send())
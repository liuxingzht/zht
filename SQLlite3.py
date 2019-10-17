# -*- coding: utf-8 -*-
#引入sqlite3包
import sqlite3
#打开数据库文件test.db
conn=sqlite3.connect('test.db')
#获取游标
cur=conn.cursor()
#建一个demo表
#cur.execute("create table demo(num int ,str varchar(20));")
#插入记录
cur.execute("insert into demo values (%d,'%s')" % (1,'aaa'))
cur.execute("insert into demo values (%d,'%s')" % (2,'bbb'))
cur.execute("insert into demo values (%d,'%s')" % (3,'ccc'))

#更新一条记录
cur.execute("update demo set str='%s' where num=%d" % ('ddd',3))
#删除记录
cur.execute("delete from demo where num=2")
#查询
cur.execute("select * from demo;")
rows=cur.fetchall()
print("number of records:",len(rows))
for i in rows:
    print(i)


#提交事务
conn.commit()
#关闭游标对象
cur.close()
#关闭数据库链接
conn.close()

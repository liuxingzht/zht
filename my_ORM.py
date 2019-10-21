# -*- coding: utf-8 -*-
from peewee import *
import sys
from importlib import reload
reload(sys)
import os
if os.path.exists('sampleDB.db'):
    os.remove('sampleDB.db')
#建立一个SQLite数据库引擎对象，该引擎打开说句库sampleDB.db文件
db=SqliteDatabase("sampleDB.db")
#定义一个ORM基类，并在基类中指定ORM指定的数据库
class BaseModel(Model):
    class Meta:
        database =db
#定义一个course表，继承自BaseModel
class Course(BaseModel):
    id=PrimaryKeyField()
    title=CharField(null = False)
    period=IntegerField()
    description=CharField()
class Meta:
    order_by=('title',) #定义数据库中的表名
    db_table='course'
#定义一个teacher表，继承自BaseModel
class Teacher(BaseModel):
    id=PrimaryKeyField()
    name=CharField(null=False)
    gender=BooleanField()
    address=CharField()
    course_id=ForeignKeyField(Course,to_field="id",related_name="course")
    class Meta:
        order_by=('name',)
        db_table='teacher'

#建表，只需要建一次
Course.create_table()
Teacher.create_table()
#新添加行
Course.create(id=1,title='经济学',period=320,description='文理科学生均可参选')
Course.create(id=2,title='大学英语',period=300,description='大一学生必修课')
Course.create(id=3,title='哲学',period=100,description='必修课')
Course.create(id=104,title='编译原理',period=100,description='计算机系选修')
Teacher.create(name='小明',gender=True,address='...',course_id=1)
Teacher.create(name='小王',gender=True,address='...',course_id=3)
Teacher.create(name='小花',gender=False,address='...',course_id=2)

#查询一行
record=Course.get(Course.title=='大学英语')
print("课程：%s,学时:%d" % (record.title,record.period))
#更新
record.period=200
record.save()
#删除
record.delete_instance()
#查询所有记录
courses=Course.select()
#带条件查询，并将结果按period字段进行排序
courses=Course.select().where(Course.id<10).order_by(Course.period.desc())
#统计所有课程的平均学识
total=Course.select(fn.Avg (Course.period).alias('avg_period'))
#更新多个记录
Course.update(period=300).where(Course.id>100).execute()
#多表链接操作，Peewee会自动根据ForeighdeyField的外键定义进行链接：
Record=Course.select().join(Teacher).where(Teacher.gender==True)
for i in Record:
    print(i.id, i.title, i.period, i.description)


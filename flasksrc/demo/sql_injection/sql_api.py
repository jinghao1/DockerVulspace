import time
from demo.model import UserMysql,UserPostgreSQL,Usersqlite
from flask import Flask,request
from demo.common import SerializerJsonResponse
from demo.global_var import dt_get_value
import pymongo


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# sql injection
# Execute custom SQL statements;eg: name=song
def mysql_post_e():
    db = dt_get_value("db")
    app = dt_get_value("app")
    sqlname = request.form['name']
    sqlQuery = "select phone from muser where name='{}'".format(sqlname)

    rows = db.session.execute(sqlQuery, bind=db.get_engine(app, 'mysqlDb'))
    if rows:
        for line in rows:
            return SerializerJsonResponse({"phone": line[0]})
    else:
        return SerializerJsonResponse({"phone": ""})


# mysql批量执行
#  description=_("Batch execution of MySQL statements;eg: name=song,phone1=13322443212"),
def mysql_post_many():
    db = dt_get_value("db")
    app = dt_get_value("app")
    ser = request.form
    if ser:
        userName = ser['name']
        userPhone = ser['phone1']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    rangePhone = int(time.time())

    args = [
        UserMysql(name=userName, phone=rangePhone),
        UserMysql(name="name_=''%flask"+str(rangePhone), phone=userPhone)
    ]
    print(args)
    rows = db.session.bulk_save_objects(args)

    exec_end = db.session.commit()
    return SerializerJsonResponse({"result": exec_end})


# sqlite3 excute
#         description=_("Execute custom SQL statements;eg: name=song"),
def sql_post_r():
    db = dt_get_value("db")
    app = dt_get_value("app")
    ser = request.form
    if ser:
        sqlQuery = "select phone from suser where name='{}'".format(ser['name'])
    else:
        return SerializerJsonResponse(None, 202, "params error")
    rows = db.session.execute(sqlQuery, bind=db.get_engine(app, 'sqlite3'))

    if rows:
        for line in rows:
            return SerializerJsonResponse({"phone": line[0]})
    else:
        return SerializerJsonResponse({"phone": ""})


# sqlite3 executemany
#                   description=_("Batch execution of sqlite3 executemany statements;eg: phone1=15523421232"),
def sql_post_executemany_sql():
    db = dt_get_value("db")
    ser = request.form
    if ser:
        phone1 = ser['phone1']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    db.session.execute(
        Usersqlite.__table__.insert(),
        [{"name": '张三1' + str(i), "phone": phone1} for i in range(10)]
    )
    db.session.commit()
    return SerializerJsonResponse({})


# sqlite3 executescript
# description=_("Execute custom SQL statements of cursor.executescript,update phone1 by name;eg: phone1=15523421232,name=song"),
def sql_post_executescript():
    db = dt_get_value("db")
    ser = request.form
    if ser:
        phone1 = ser['phone1']
        name = ser['name']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    res = db.session.query(Usersqlite).filter(Usersqlite.phone == phone1).update({"name": name})
    db.session.commit()
    return SerializerJsonResponse(res)


# Execute custom SQL of pysql statements ;eg: sql=song
def pysql_post_excute():
    db = dt_get_value("db")
    app = dt_get_value("app")
    ser = request.form
    if ser:
        sqlQuery = "select phone from puser where name='{}'".format(ser['name'])
    else:
        return SerializerJsonResponse(None, 202, "params error")
    rows = db.session.execute(sqlQuery, bind=db.get_engine(app, 'pySqlDb'))
    print(dir(db.session))
    if rows:
        for line in rows:
            return SerializerJsonResponse({"phone": line[0]})
    else:
        return SerializerJsonResponse({"phone": ""})


# pysql 批量执行
# description=_("Execute custom SQL of pysql statements ;eg: name=song,phone1=16654321232,id=100"),
def pysql_post_many():
    db = dt_get_value("db")
    ser = request.form
    if ser:
        userName = ser['name']
        userPhone = ser['phone1']
        userId = ser['id']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    userId_next = int(userId)+1
    rangePhone = int(time.time())
    args = [
        dict(id=userId, name=userName, phone=rangePhone),
        dict(id=userId_next, name="name_pysql", phone=userPhone)
    ]
    db.session.bulk_insert_mappings(UserPostgreSQL, args)
    exec_end = db.session.commit()
    return SerializerJsonResponse({"result": exec_end})


# mongo sql excute
def mongo_post_excute():

    ser = request.form

    if ser:
        sqlQuery = "db.guser.find({name:song})"
    else:
        return SerializerJsonResponse(None, 202, "params error")
    client = pymongo.MongoClient(host="localhost", port=27017)

    ## 指定数据库
    db = client.test

    # 指定集合（类似于表）
    collection = db.guser

    # 插入数据
    student = {
        "id": "10001",
        "name": "Jordan",
        "age": "20",
        "gender": "male"
    }
    rows = collection.insert_one(student)

    print(rows)
    if rows:
        for line in rows:
            print(line)
            return SerializerJsonResponse({"phone": line[0]})
    else:
        return SerializerJsonResponse({"phone": ""})
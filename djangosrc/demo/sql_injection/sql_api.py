
import builtins
import inspect
from typing import TextIO
from django.db import connections,connection
from django.http import JsonResponse
from demo.utils import extend_schema_with_envcheck
from demo.serializer.serializers import _SqlArgsSerializer,_SuccessSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import api_view
from demo.common import SerializerJsonResponse


# mysql injection
@extend_schema_with_envcheck([_SqlArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('mysql Execute mysql.execute'),
                             description=_("Execute custom SQL statements;eg: name=song"),
                             tags=[_('mysql-injection')])
@api_view(['POST'])
def mysql_post_e(request):
    ser = _SqlArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        sqlQuery = "select phone from muser where name='{}'".format(ser.validated_data['name'])
    else:
        return SerializerJsonResponse(None, 202, "params error")
    with connections['default'].cursor() as cursor:
        execEnd = cursor.execute(sqlQuery)
        endData = cursor.fetchone()

    return SerializerJsonResponse({"phone": endData[0]})


# mysql批量执行
@extend_schema_with_envcheck([_SqlArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('mysql insert mysql.executemany'),
                             description=_("Batch execution of MySQL statements;eg: name=song,phone1=13322443212"),
                             tags=[_('mysql-injection')])
@api_view(['POST'])
def mysql_post_many(request):
    ser = _SqlArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        userName = ser.validated_data['name']
        userPhone = ser.validated_data['phone1']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    exec_end = []
    with connections['default'].cursor() as cursor:

        sql = "insert into muser(name, phone) values( % s, % s) "
        args = [(userName, 100), ("name1", userPhone)]
        try:
            exec_end = cursor.executemany(sql, args)
        except Exception as e:
            print("执行Mysql:")

    print("----------")
    return SerializerJsonResponse({"result": exec_end})


# sqlite3 excute
@extend_schema_with_envcheck([_SqlArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('sqlite3 excute injection  '),
                             description=_("Execute custom SQL statements;eg: name=song"),
                             tags=[_('mysql-injection')])
@api_view(['POST'])
def sql_post_r(request):
    ser = _SqlArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        sqlQuery = "select phone from suser where name='{}'".format(ser.validated_data['name'])

    else:
        return SerializerJsonResponse(None, 202, "params error")

    with connections['sqlite3'].cursor() as cursor:
        execEnd = cursor.execute(sqlQuery)
        endData = cursor.fetchone()
    print("----------")
    print(execEnd)
    print(endData)
    return SerializerJsonResponse({"phone": endData[0]})


# sqlite3 executemany
@extend_schema_with_envcheck([_SqlArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('sqlite3 executemany insert  '),
                             description=_("Batch execution of sqlite3 executemany statements;eg: phone1=15523421232"),
                             tags=[_('mysql-injection')])
@api_view(['POST'])
def sql_post_executemany_sql(request):

    ser = _SqlArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        phone1 = ser.validated_data['phone1']
    else:
        return SerializerJsonResponse(None, 202, "params error")

    sql = "insert into suser (name, phone) values (?, ?);"
    data_list = [('张三1', phone1), ('李四1', 16655443311)]
    with connections['sqlite3'].cursor() as cursor:
        end = cursor.executemany(sql, data_list)
    return SerializerJsonResponse({})


# sqlite3 executescript
@extend_schema_with_envcheck([_SqlArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('sqlite3 executescript update  '),
                             description=_("Execute custom SQL statements of cursor.executescript,update phone1 by name;eg: phone1=15523421232,name=song"),
                             tags=[_('mysql-injection')])
@api_view(['POST'])
def sql_post_executescript(request):

    ser = _SqlArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        phone1 = ser.validated_data['phone1']
        name = ser.validated_data['name']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    sql_script = "update suser set name='{}' where phone={}".format(name,phone1)
    print(sql_script)
    with connections['sqlite3'].cursor() as cursor:
        end = cursor.executescript(sql_script)
    print(end)
    return SerializerJsonResponse({})


def no_hook_fun(request):
    return JsonResponse({
        "status": "201"
    })


@extend_schema_with_envcheck([_SqlArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('pysql execute   '),
                             description=_("Execute custom SQL of pysql statements ;eg: name=song"),
                             tags=[_('mysql-injection')])
@api_view(['POST'])
def pysql_post_excute(request):

    ser = _SqlArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        sqlQuery = "select phone from puser where name='{}'".format(ser.validated_data['name'])
    else:
        return SerializerJsonResponse(None, 202, "params error")
    with connections['pysql'].cursor() as cursor:
        execEnd = cursor.execute(sqlQuery)
        endData = cursor.fetchone()
    print("----------")
    print(execEnd)
    print(endData)
    return SerializerJsonResponse({"phone": endData[0]})


# pysql 批量执行
@extend_schema_with_envcheck([_SqlArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('pysql execute   '),
                             description=_("Execute custom SQL of pysql statements ;eg: name=song,phone1=16654321232,id=100"),
                             tags=[_('mysql-injection')])
@api_view(['POST'])
def pysql_post_many(request):
    ser = _SqlArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        userName = ser.validated_data['name']
        userPhone = ser.validated_data['phone1']
        userId = ser.validated_data['id']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    exec_end = []

    with connections['pysql'].cursor() as cursor:

        sql = "insert into puser(id, name, phone) values( %s,  %s, %s) "
        args = [(userId, userName, "100"), (str(int(userId)+1), "name1", userPhone)]
        try:
            exec_end = cursor.executemany(sql, args)
        except Exception as e:
            print(e)
            exec_end = 0

    print("----------")
    return SerializerJsonResponse(exec_end)



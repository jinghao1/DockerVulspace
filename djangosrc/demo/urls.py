from django.urls import path
from . import views
from demo.exec_code import exec_api
from demo.exec_command import cmd_api
from demo.sql_injection import sql_api

urlpatterns = [
    path('get_open', views.index_get_r),
    path('post_open', views.index_post_r),
    # PostgreSQL
    path('postgresql_post_excute', sql_api.pysql_post_excute),
    path('postgresql_post_many', sql_api.pysql_post_many),
    # mysql
    path('mysql_post_exec', sql_api.mysql_post_e),
    path('mysql_post_many', sql_api.mysql_post_many),
    # sqlite
    path('sqlite3_post', sql_api.sql_post_r),
    path('sqlite3_post_executemany_sql', sql_api.sql_post_executemany_sql),
    path('sqlite3_post_executescript', sql_api.sql_post_executescript),
    # cmd exec
    path('exec_post_e', cmd_api.exec_post_e),
    path('exec_post_popen', cmd_api.exec_post_popen),
    path('exec_post_subprocess', cmd_api.exec_post_subprocess),
    path('cmd_exec', cmd_api.cmd_exec),
    # code exec
    path('eval_post_e', exec_api.eval_post_e),
    path('yaml_post_e', exec_api.yaml_post_e),
]
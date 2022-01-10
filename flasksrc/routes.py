from os.path import dirname, join, realpath
from demo import views
from demo.sql_injection import sql_api
from demo.exec_code import exec_api
from demo.exec_command import cmd_api
from demo.xss import xss_fun
from demo.xxe import xxe_fun
from demo.ssrf import ssrf_fun
from demo.deserialization import serializ_api
from demo.ldap import ldap
from demo.crypto import crypto

DIR_PATH = dirname(realpath(__file__))


def setup_routes(app):
    # app.add_url_rule('/', 'index', views.index_get_r)
    app.add_url_rule("/demo/get_open", view_func=views.index_get_r, methods=["GET"])
    app.add_url_rule("/demo/post_open", view_func=views.index_post_r, methods=["POST"])
    # PostgreSQL
    app.add_url_rule("/demo/postgresql_post_excute", view_func=sql_api.pysql_post_excute, methods=["POST"])
    app.add_url_rule("/demo/postgresql_post_many", view_func=sql_api.pysql_post_many, methods=["POST"])
    # mysql
    app.add_url_rule("/demo/mysql_post_exec", view_func=sql_api.mysql_post_e, methods=["POST"])
    app.add_url_rule("/demo/mysql_post_many", view_func=sql_api.mysql_post_many, methods=["POST"])
    # sqlite
    app.add_url_rule("/demo/sqlite3_post", view_func=sql_api.sql_post_r, methods=["POST"])
    app.add_url_rule("/demo/sqlite3_post_executemany_sql", view_func=sql_api.sql_post_executemany_sql, methods=["POST"])
    app.add_url_rule("/demo/sqlite3_post_executescript", view_func=sql_api.sql_post_executescript, methods=["POST"])
    # mongo
    app.add_url_rule("/demo/mongo_find", view_func=sql_api.mongo_find, methods=["GET", "POST"])
    # 增加 命令执行
    app.add_url_rule("/demo/exec_post_e", view_func=cmd_api.exec_post_e, methods=["POST"])
    app.add_url_rule("/demo/exec_post_popen", view_func=cmd_api.exec_post_popen, methods=["POST"])

    app.add_url_rule("/demo/exec_post_subprocess", view_func=cmd_api.exec_post_subprocess, methods=["POST"])
    app.add_url_rule("/demo/cmd_exec", view_func=cmd_api.cmd_exec, methods=["POST"])

    # code exec
    app.add_url_rule("/demo/eval_post_e", view_func=exec_api.eval_post_e, methods=["POST"])
    app.add_url_rule("/demo/yaml_post_e", view_func=exec_api.yaml_post_e, methods=["POST"])

    # xss
    # safe
    app.add_url_rule("/demo/xss_template", view_func=xss_fun.xssTemplate, methods=["GET"])
    # safe
    app.add_url_rule("/demo/xss_template_string", view_func=xss_fun.xssTemplateString, methods=["GET"])
    # have vul
    app.add_url_rule("/demo/xss_return", view_func=xss_fun.xssReturn, methods=["GET"])

    # xxe have vul
    app.add_url_rule("/demo/xxe_login", view_func=xxe_fun.doLoginXXE, methods=["POST"])

    # ssrf urllib
    app.add_url_rule("/demo/urllib_ssrf", view_func=ssrf_fun.urllib_ssrf, methods=["GET"])
    app.add_url_rule("/demo/request_ssrf", view_func=ssrf_fun.request_ssrf, methods=["GET"])

    # deserialization
    # pickle
    app.add_url_rule("/demo/make_pickle_data", view_func=serializ_api.makePickleData, methods=["POST"])
    app.add_url_rule("/demo/get_pickle_data", view_func=serializ_api.getPickleData, methods=["POST"])
    # pickle read from file
    app.add_url_rule("/demo/make_pickle_file", view_func=serializ_api.savePickleInFile, methods=["POST"])
    app.add_url_rule("/demo/get_pickle_file", view_func=serializ_api.exutePickleFromFile, methods=["POST"])
    # marshal
    app.add_url_rule("/demo/make_marshal_data", view_func=serializ_api.makeMarshalData, methods=["POST"])
    app.add_url_rule("/demo/get_marshal_data", view_func=serializ_api.getMarshalData, methods=["POST"])

    # ldap
    app.add_url_rule("/demo/ldap_search", view_func=ldap.ldap_search, methods=["GET", "POST"])
    app.add_url_rule("/demo/ldap_safe_search", view_func=ldap.ldap_safe_search, methods=["GET", "POST"])
    app.add_url_rule("/demo/ldap3_search", view_func=ldap.ldap3_search, methods=["GET", "POST"])
    app.add_url_rule("/demo/ldap3_safe_search", view_func=ldap.ldap3_safe_search, methods=["GET", "POST"])

    # crypto-bad-cipher
    app.add_url_rule("/demo/crypto/aes", view_func=crypto.pycryptodome_aes, methods=["GET", "POST"])
    app.add_url_rule("/demo/crypto/blowfish", view_func=crypto.pycryptodome_blowfish, methods=["GET", "POST"])
    app.add_url_rule("/demo/crypto/des", view_func=crypto.pycryptodomex_des, methods=["GET", "POST"])
    app.add_url_rule("/demo/cryptox/blowfish", view_func=crypto.pycryptodomex_blowfish, methods=["GET", "POST"])
    app.add_url_rule("/demo/cryptox/des", view_func=crypto.pycryptodome_des, methods=["GET", "POST"])

import ldap3
from flask import request
from ldap3.utils.conv import escape_filter_chars


def ldap_search():
    username = request.args.get('username', '')
    password = request.args.get('password', '')

    ldap_srv = ldap3.Server("ldap://ldap:10389")
    ldap_conn = ldap3.Connection(ldap_srv, user="cn=admin,dc=planetexpress,dc=com", password="GoodNewsEveryone",
                                 auto_bind=True)

    search_filter = "(&(cn=%s)(userPassword=%s))" % (username, password)
    exists = ldap_conn.search("dc=planetexpress,dc=com", search_filter)
    if not exists:
        return "403"
    return "200"


def ldap_safe_search():
    username = request.args.get('username', '')
    password = request.args.get('password', '')

    ldap_srv = ldap3.Server("ldap://ldap:10389")
    ldap_conn = ldap3.Connection(ldap_srv, user="cn=admin,dc=planetexpress,dc=com", password="GoodNewsEveryone",
                                 auto_bind=True)

    username = escape_filter_chars(username)
    password = escape_filter_chars(password)

    search_filter = "(&(cn=%s)(userPassword=%s))" % (username, password)
    exists = ldap_conn.search("dc=planetexpress,dc=com", search_filter)
    if not exists:
        return "403"
    return "200"

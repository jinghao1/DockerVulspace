import os
import socket
import subprocess
import sys

from rasp.filter import is_http, is_sql
from rasp.log import logger
from rasp.processor import extract_printable
from rasp.smith import smith_hook
from rasp.ext import scope
if sys.version_info >= (3, 0):
    import builtins
    from urllib.request import urlopen
else:
    import __builtin__ as builtins
    from urllib2 import urlopen

logger.info("python probe start")

scope.enter_scope(scope.SCOPE_AGENT)
subprocess.Popen.__init__ = smith_hook(subprocess.Popen.__init__, 1, 0, constructor=True, can_block=True)

os.system = smith_hook(os.system, 1, 1, can_block=True)
os.execv = smith_hook(os.execv, 1, 7, can_block=True)
os.execve = smith_hook(os.execve, 1, 8, can_block=True)
os.spawnv = smith_hook(os.spawnv, 1, 15, can_block=True)
os.spawnve = smith_hook(os.spawnve, 1, 16, can_block=True)
os.spawnvp = smith_hook(os.spawnvp, 1, 17, can_block=True)
os.spawnvpe = smith_hook(os.spawnvpe, 1, 18, can_block=True)

if sys.version_info < (3, 0):
    os.popen = smith_hook(os.popen, 1, 2, can_block=True)

builtins.open = smith_hook(builtins.open, 0, 3, check_recursion=True)

os.open = smith_hook(os.open, 1, 19)
os.remove = smith_hook(os.remove, 1, 20)
os.rmdir = smith_hook(os.rmdir, 1, 21)
os.rename = smith_hook(os.rename, 1, 22)
os.listdir = smith_hook(os.listdir, 1, 23)

if sys.version_info >= (3, 5):
    os.scandir = smith_hook(os.scandir, 1, 24)

socket.socket.connect = smith_hook(socket.socket.connect, 4, 1)

socket.socket.sendall = smith_hook(
    socket.socket.sendall,
    4,
    0,
    processors={bytes: extract_printable},
    filters=[is_http, is_sql]
)

socket.getaddrinfo = smith_hook(socket.getaddrinfo, 4, 2)
socket.gethostbyname = smith_hook(socket.gethostbyname, 4, 3)

builtins.eval = smith_hook(builtins.eval, 0, 0, inherit=True)
builtins.compile = smith_hook(builtins.compile, 0, 2)

urlopen = smith_hook(urlopen, 6, 0)

if sys.version_info >= (3, 0):
    from http.client import HTTPConnection
    HTTPConnection.__init__ = smith_hook(HTTPConnection.__init__, 6, 1, constructor=True)

try:
    from flask import Flask
    from rasp.processor import flask_request_processor

    Flask.dispatch_request = smith_hook(Flask.dispatch_request, 5, 0, request_processor=flask_request_processor)

except ImportError:
    pass

try:
    from django.core.handlers.base import BaseHandler
    from rasp.processor import django_request_processor2

    BaseHandler.get_response = smith_hook(
        BaseHandler.get_response,
        7,
        0,
        request_processor=django_request_processor2
    )

except ImportError:
    pass

try:
    from pymongo import version_tuple
    from pymongo.collection import Collection

    if version_tuple >= (3, 0):
        Collection.find = smith_hook(Collection.find, 8, 0, can_block=True)
        Collection.insert_one = smith_hook(Collection.insert_one, 8, 1, can_block=True)
        Collection.insert_many = smith_hook(Collection.insert_many, 8, 2, can_block=True)
        Collection.delete_one = smith_hook(Collection.delete_one, 8, 3, can_block=True)
        Collection.delete_many = smith_hook(Collection.delete_many, 8, 4, can_block=True)
        Collection.update_one = smith_hook(Collection.update_one, 8, 5, can_block=True)
        Collection.update_many = smith_hook(Collection.update_many, 8, 6, can_block=True)
        Collection.aggregate = smith_hook(Collection.aggregate, 8, 7, can_block=True)

except ImportError:
    pass

try:
    from pymysql.cursors import Cursor

    Cursor.execute = smith_hook(Cursor.execute, 9, 0, can_block=True)
    Cursor.executemany = smith_hook(Cursor.executemany, 9, 1, can_block=True)

except ImportError:
    pass

try:
    from sqlalchemy.orm.session import Session

    def transaction(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except RuntimeError:
                args[0].rollback()
                raise

        return wrapper

    Session.commit = transaction(Session.commit)

except ImportError:
    pass


from rasp.ext.base_middleware import BaseMiddleware
BaseMiddleware()
logger.info("------begin hook-----")

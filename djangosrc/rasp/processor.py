import base64
import sys
import platform
from curses import ascii

from rasp import logger

if sys.version_info >= (3, 0):
    from urllib.parse import unquote
else:
    from urllib import unquote

_version = platform.python_version()


def _base64_encode(data):
    encoded = base64.b64encode(data)

    if sys.version_info < (3, 0):
        return encoded

    return encoded.decode()


def _exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error("request processor error: %s", e)
            return {}

    return wrapper


try:
    from flask import request

    @_exception_handler
    def flask_request_processor(*args, **kwargs):
        result = {
            'frame': 'Flask py ' + _version,
            'url': unquote(request.url),
            'method': request.method,
            'headers': {k: v for k, v in request.headers.items()},
            'cookies': request.cookies.to_dict() if hasattr(request.cookies,"to_dict") else "",
            'params': request.args.to_dict()  if hasattr(request.args,"to_dict") else "",
        }

        if request.method != 'POST':
            return result

        if request.json:
            result['body'] = request.json
            return result

        if not request.form and not request.files:
            result['data'] = _base64_encode(request.data[:4096])
            return result

        if request.form:
            result['body'] = request.form.to_dict() if hasattr(request.form,"to_dict") else {}

        if request.files:
            result['files'] = {
                '{}:{}'.format(k, v.filename): _base64_encode(v.stream.read())
                for k, v in request.files.items()
            }

        return result

except ImportError:
    pass

try:
    from django import VERSION
    from django.core.handlers.wsgi import WSGIRequest

    @_exception_handler
    def django_request_processor2(*args, **kwargs):
        wsgi_request = args[1]
        print("test agent =====")
        print(wsgi_request)
        return {
                'frame': 'Django py ' + _version,
                'url': unquote(wsgi_request.build_absolute_uri()),
                'method': wsgi_request.method,
                'headers': {k: v for k, v in wsgi_request.headers.items()} if VERSION >= (2, 2) else {},
                'cookies': wsgi_request.COOKIES,
                'params': wsgi_request.GET.dict(),
            }

except ImportError:
    pass


def extract_printable(data):
    return bytearray(filter(ascii.isprint, bytearray(data))).decode()

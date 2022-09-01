import re
import struct


def is_http(*args, **kwargs):
    if not isinstance(args[1], bytes):
        return False

    return re.search(
        br'^(?:GET|POST|HEAD|PATCH|PUT|DELETE|OPTIONS|CONNECT|TRACE).+HTTP/1\.[0,1]\r\nHost',
        args[1],
        re.DOTALL
    ) is not None


def is_sql(*args, **kwargs):
    data = args[1]

    if not isinstance(data, bytes):
        return False

    if len(data) < 5:
        return False

    query_len, sql_type = struct.unpack('<iB', data[:5])

    if sql_type != 3 and sql_type != 23:
        return False

    return re.search(
        br'^select.*from|^update.*set|delete.*from|insert.*into.*values',
        data[5:],
        re.DOTALL | re.IGNORECASE
    ) is not None

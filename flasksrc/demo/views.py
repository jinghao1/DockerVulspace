import json,os,time
from demo.common import SerializerJsonResponse
from aiohttp.web import Request, HTTPFound
from flask import Flask,request

def func(a, b):
    return a / b


def func2(filePath,n=3):
    path_arr = filePath.split("**")
    path_arr.append(n)
    return path_arr


def func3_open(end_path):
    endData = {}
    print(end_path)

    with open(end_path, encoding='utf-8') as f:
        # line = f.readline()
        line = f.read()
        d = json.loads(line)
        name = d['name']
        telephone = d['telphone']
        endData['name'] = name
        endData['telephone'] = telephone
        f.close()
    print(endData)
    return endData


def index_get_r():
    print(request.args)
    filePath = request.args.get("name", "")
    print(filePath)
    filePath = filePath.lower()
    path_arr = func2(filePath, ".json")
    filePath = "".join(path_arr)

    curDir = os.path.dirname(__file__)
    after_path = "./file/{}".format(filePath)
    end_path = os.path.join(curDir,after_path)
    endData = func3_open(end_path)
    return SerializerJsonResponse(endData)


def index_post_r():

    filePath = request.form['name']

    curDir = os.path.dirname(__file__)

    end_path = os.path.join(curDir, filePath)

    endData = {}
    with open(end_path, encoding='utf-8') as f:
        endData['content'] = f.read()
        f.close()

    return SerializerJsonResponse(endData)


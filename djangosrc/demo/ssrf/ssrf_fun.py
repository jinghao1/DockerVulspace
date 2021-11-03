from flask import Flask, request
import urllib
import requests,json
import ssl
from demo.common import SerializerJsonResponse
context = ssl._create_unverified_context()

# eg:url=file:///etc/passwd
def urllib_ssrf():
    url = request.args.get("url","https://www.baidu.com")
    try:
        info = urllib.request.urlopen(url, context=context).read()
        info = info.decode("utf-8")
        # print(info)
    except urllib.error.URLError as e:
        info = str(e)
        # print(e)
    return SerializerJsonResponse({"status": 201,"result": info})


# url=http://192.168.2.168
# 内网遍历
def request_ssrf():
    url = request.args.get("url", "https://www.baidu.com")
    try:
        res = requests.get(url, timeout=10)
        info = str(res.content.decode("utf-8"))
    except Exception as e:
        info = str(e)
    # print(info)
    return SerializerJsonResponse({"status": 201, "result": info})
from flask import Flask, request
from lxml import etree
from demo.common import SerializerJsonResponse
USERNAME = "username"
PASSWORD = "passWd"


# eg: Content-Type=application/xml;charset=utf-8,post body: <user><username>username</username><password>passWd</password></user>
# payload xxe
# <?xml version="1.0" encoding="utf-8"?>
#  <!DOCTYPE Anything [
#  <!ENTITY xxe SYSTEM "file:///etc/passwd">
#  ]>
#  <user>
#   <username>&xxe;</username>
#   <password>
#     yzx
#   </password>
#  </user>
def doLoginXXE():
    result = None
    try:
        # 漏洞修复--禁用外部实体  resolve_entities=False
        etree.XMLParser
        # tree = etree.fromstring(request.data,etree.XMLParser(resolve_entities=False))
        tree = etree.fromstring(request.data)  # 有漏洞
        # 遍历xml结构内容
        for childa in tree:
            print(childa.tag, childa.text, childa.attrib)
            if childa.tag == "username":
                username = childa.text
                print(username)
            if childa.tag == "password":
                password = childa.text
                print(password)
        if username == USERNAME and password == PASSWORD:
            result = "<result><code>%d</code><msg>%s</msg></result>".format(1, username)
        else:
            result = "<result><code>%d</code><msg>%s</msg></result>".format(0, username)
    except Exception as Ex:
        result = "<result><code>%d</code><msg>%s</msg></result>".format(3, str(Ex))
    end = {
        "result": result,
        "status": 201,
        "header": {'Content-Type': 'text/xml;charset=UTF-8'}
    }
    return SerializerJsonResponse(end)



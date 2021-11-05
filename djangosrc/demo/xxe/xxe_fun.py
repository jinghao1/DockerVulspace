from rest_framework.decorators import api_view
from lxml import etree

from demo.common import SerializerJsonResponse
from django.utils.translation import gettext_lazy as _
from demo.utils import extend_schema_with_envcheck
from demo.serializer.serializers import _WebSerializer,_SuccessSerializer

from django.http import HttpResponse


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
@extend_schema_with_envcheck([_WebSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('xxe return'),
                             description=_("Execute xxe;#将结果展示到页面 eg: Content-Type=application/xml;charset=utf-8;  post body: <user><username>username</username><password>passWd</password></user>" ),
                             tags=[_('xxe')])
@api_view(['POST'])
def doLoginXXE(request):
    try:
        # 漏洞修复--禁用外部实体  resolve_entities=False
        # tree = etree.fromstring(request.data,etree.XMLParser(resolve_entities=False))

        username = None
        password = None

        tree = etree.fromstring(request.body)  # 有漏洞

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
            result = "<result><code>{}</code><msg>{}</msg></result>".format(1, username)
        else:
            result = "<result><code>{}</code><msg>{}</msg></result>".format(0, username)
    except Exception as Ex:
        result = "<result><code>{}</code><msg>{}</msg></result>".format(3, str(Ex))
    return HttpResponse(result)

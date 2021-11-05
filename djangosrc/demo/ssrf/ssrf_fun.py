from rest_framework.decorators import api_view
import urllib
import requests,json
import ssl
from demo.common import SerializerJsonResponse
from django.utils.translation import gettext_lazy as _
from demo.utils import extend_schema_with_envcheck
from demo.serializer.serializers import _WebSerializer,_SuccessSerializer
context = ssl._create_unverified_context()


# eg:url=file:///etc/passwd
@extend_schema_with_envcheck([_WebSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('ssrf  urllib.request.urlopen'),
                             description=_("Execute ssrf;eg: url=https://www.sina.cn    eg:url=file:///etc/passwd" ),
                             tags=[_('ssrf')])
@api_view(['GET'])
def urllib_ssrf(request):
    ser = _WebSerializer(data=request.GET)
    if ser.is_valid(True):
        url = ser.validated_data['url']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    try:
        info = urllib.request.urlopen(url, context=context).read()
        info = info.decode("utf-8")
        # print(info)
    except urllib.error.URLError as e:
        info = str(e)
        # print(e)
    return SerializerJsonResponse(info)


# url=http://192.168.2.168
# 内网遍历
@extend_schema_with_envcheck([_WebSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('ssrf requests.get'),
                             description=_("Execute ssrf; eg: url=url=http://192.168.2.168"),
                             tags=[_('ssrf')])
@api_view(['GET'])
def request_ssrf(request):
    ser = _WebSerializer(data=request.GET)
    if ser.is_valid(True):
        url = ser.validated_data['url']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    try:
        res = requests.get(url, timeout=10)
        info = str(res.content.decode("utf-8"))
    except Exception as e:
        info = str(e)
    # print(info)
    return SerializerJsonResponse(info)
from django.shortcuts import render
from demo.common import SerializerJsonResponse
from rest_framework.decorators import api_view
from django.utils.translation import gettext_lazy as _
from demo.utils import extend_schema_with_envcheck
from demo.serializer.serializers import _WebSerializer,_SuccessSerializer


# safe
@extend_schema_with_envcheck([_WebSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('xss render'),
                             description=_("Execute xss;eg: content=<script>alert(1）</script>" ),
                             tags=[_('xss')])
@api_view(['GET'])
def xssTemplate(request):
    ser = _WebSerializer(data=request.GET)
    if ser.is_valid(True):
        content = ser.validated_data['content']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    return render(request, 'xss_index.html', {"contents": content})


# no safe
@extend_schema_with_envcheck([_WebSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('xss return'),
                             description=_("Execute xss;eg: content=<script>alert(1）</script>" ),
                             tags=[_('xss')])
@api_view(['GET'])
def xssReturn(request):
    ser = _WebSerializer(data=request.GET)
    if ser.is_valid(True):
        content = ser.validated_data['content']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    return SerializerJsonResponse(content)
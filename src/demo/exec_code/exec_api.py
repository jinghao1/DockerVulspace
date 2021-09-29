import json,os,yaml,subprocess

from demo.utils import extend_schema_with_envcheck
from demo.serializer.serializers import _DocumentArgsSerializer,_SuccessSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import api_view
from demo.common import SerializerJsonResponse


# 代码执行
@extend_schema_with_envcheck([_DocumentArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('code Execute eval'),
                             description=_("code execution api of eval;eg: code=__ import __('os').system('whoami') "),
                             tags=[_('code exec')])
@api_view(['POST'])
def eval_post_e(request):
    ser = _DocumentArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        code = ser.validated_data['code']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    end = eval(code)
    return SerializerJsonResponse(end)


# yaml 代码执行
@extend_schema_with_envcheck([_DocumentArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('code Execute yaml'),
                             description=_("code execution api of yaml.unsafe_load;eg: code=whoami"),
                             tags=[_('code exec')])
@api_view(['POST'])
def yaml_post_e(request):
    ser = _DocumentArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        code = ser.validated_data['code']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    exp = """!!python/object/apply:os.system ['{}']""".format(code)
    # yaml.__version__ < 5.1b1 hook yaml.load()
    end = yaml.unsafe_load(exp)
    return SerializerJsonResponse(end)




import json,os,yaml,subprocess
from django.http import JsonResponse
from demo.utils import extend_schema_with_envcheck
from demo.serializer.serializers import _DocumentArgsSerializer,_SuccessSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import api_view
from demo.common import SerializerJsonResponse


# 命令执行
@extend_schema_with_envcheck([_DocumentArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('command Execute os.system'),
                             description=_("System command execution api of os.system;eg: code=whoami"),
                             tags=[_('cmd exec')])
@api_view(['POST'])
def exec_post_e(request):
    ser = _DocumentArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        code = ser.validated_data['code']
    else:
        return SerializerJsonResponse(None,202,"params error")

    new_code = "ping -c1 {}".format(code)
    end = os.system(new_code)
    return SerializerJsonResponse(end)


# 命令执行
@extend_schema_with_envcheck([_DocumentArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('command Execute os.popen'),
                             description=_("System command execution api of os.popen and get List of all files in the folder; eg: code=ls"),
                             tags=[_('cmd exec')])
@api_view(['POST'])
def exec_post_popen(request):

    ser = _DocumentArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        code = ser.validated_data['code']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    # 文件夹内所有文件的列表.
    files = os.popen(code).readlines()
    return SerializerJsonResponse(files)


# 子进程命令执行
@extend_schema_with_envcheck([_DocumentArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('command Execute subprocess.Popen'),
                             description=_("System command execution api of os.popen ; eg: cmd=cat,name=/etc/passwd"),
                             tags=[_('cmd exec')])
@api_view(['POST'])
def exec_post_subprocess(request):
    ser = _DocumentArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        cmd = ser.validated_data['cmd']
        name = ser.validated_data['name']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    # 将一个子进程的输出，作为另一个子进程的输入：
    child1 = subprocess.Popen([cmd, name],
                              stdout=subprocess.PIPE)
    child2 = subprocess.Popen(["grep", "0:0"],
                              stdin=child1.stdout,
                              stdout=subprocess.PIPE)
    out = child2.communicate()
    outInfo = out[0]
    if isinstance(outInfo,bytes):
        outInfo = str(outInfo, encoding="utf-8")
    return SerializerJsonResponse(outInfo)


# 命令执行
@extend_schema_with_envcheck([_DocumentArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('command Execute subprocess.Popen str'),
                             description=_("System command execution api of os.popen ; eg: cmd=whoami"),
                             tags=[_('cmd exec')])
@api_view(['POST'])
def cmd_exec(request):
    ser = _DocumentArgsSerializer(data=request.POST)
    if ser.is_valid(True):
        cmd = ser.validated_data['cmd']
    else:
        return SerializerJsonResponse(None, 202, "params error")
    magic = [].__class__.__base__.__subclasses__()
    ret = []
    for item in magic:
        if "<class 'subprocess.Popen'>" == str(item):
            ret = item.__init__.__globals__['os'].system(cmd)
            break
    return SerializerJsonResponse(ret)
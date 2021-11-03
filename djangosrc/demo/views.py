import json,os,time
from django.http import JsonResponse
import traceback
from demo.utils import extend_schema_with_envcheck
from demo.serializer.serializers import _FilePathArgsSerializer,_SuccessSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import api_view
from demo.common import SerializerJsonResponse


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


@extend_schema_with_envcheck([_FilePathArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('path traversal of get'),
                             description=_("Get the file content through the get parameter；eg: name=Data**"),
                             tags=[_('path-traversal')])
@api_view(['GET'])
def index_get_r(self):
    filePath = self.GET.get("name", "")
    filePath = filePath.lower()
    path_arr = func2(filePath, ".json")
    filePath = "".join(path_arr)
    end_path = "./file/{}".format(filePath)
    endData = func3_open(end_path)
    return SerializerJsonResponse(endData)


@extend_schema_with_envcheck([_FilePathArgsSerializer],
                             response_schema=_SuccessSerializer,
                             summary=_('path traversal of post'),
                             description=_("Get the file content through the get parameter；eg: name=./file/data.json"),
                             tags=[_('path-traversal')])
@api_view(['POST'])
def index_post_r(request):

    filePath = request.POST['name']
    endData = {}
    with open(filePath, encoding='utf-8') as f:
        endData['content'] = f.read()
        f.close()
    tracert = traceback.extract_stack()
    end = traceback.format_list(tracert)
    print(end)

    # traceback.print_tb(tracert_arr[-3])
    return SerializerJsonResponse(endData)


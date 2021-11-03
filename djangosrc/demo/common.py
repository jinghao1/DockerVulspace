from collections import namedtuple
from django.http import JsonResponse
from demo.serializer.serializers import _SuccessSerializer


def SerializerJsonResponse(endData=None, status=201, msg="success"):
    Res = namedtuple('we', ['status', 'msg', 'data'])
    res = Res(status=status, msg=msg, data=[endData])
    return JsonResponse(_SuccessSerializer(res).data)
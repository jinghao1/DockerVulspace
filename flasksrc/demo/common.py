from collections import namedtuple
import json
from flask import jsonify
# from django.http import JsonResponse
# from demo.serializer.serializers import _SuccessSerializer


def SerializerJsonResponse(endData=None, status=201, msg="success"):
    # Res = namedtuple('we', ['status', 'msg', 'data'])
    # res = Res(status=status, msg=msg, data=[endData])
    res = {
        "status": status,
        "msg": msg,
        "data": [endData]
    }

    return jsonify(res)
    # return JsonResponse(_SuccessSerializer(res).data)
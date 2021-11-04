from django.shortcuts import render
from demo.common import SerializerJsonResponse
from rest_framework.decorators import api_view


# safe
@api_view(['GET'])
def xssTemplate(request):
    content = request.GET.get("content","null")
    return render(request,'xss_index.html',{"contents":content})


# no safe
@api_view(['GET'])
def xssReturn(request):
    content = request.GET.get("content", "null")
    return SerializerJsonResponse(content)
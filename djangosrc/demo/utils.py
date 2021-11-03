from rest_framework.serializers import SerializerMetaclass
from django.utils.translation import get_language
from django.utils.text import format_lazy
import os
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiTypes,OpenApiResponse
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
import uuid


def _filter_query(item):

    if isinstance(item, SerializerMetaclass):
        return item
    elif isinstance(item, dict):
        return OpenApiParameter(**item)


def _filter_request_body(item):

    if isinstance(item, dict):
        item['request_only'] = True
        return OpenApiExample(**item)


def _filter_response_body(item):

    if isinstance(item, dict):
        item['response_only'] = True
        return OpenApiExample(**item)


def extend_schema_with_envcheck(querys: list = [],
                                request_bodys: list = [],
                                response_bodys: list = [],
                                response_schema=None,
                                **kwargs):
    def myextend_schema(func):

        parameters = list(filter(lambda x: x, map(_filter_query, querys)))
        request_examples = list(
            filter(lambda x: x, map(_filter_request_body, request_bodys)))
        response_examples = list(
            filter(lambda x: x, map(_filter_response_body,
                                    response_bodys)))
        examples = request_examples + response_examples
        if kwargs.get('request', None) and request_examples:
            kwargs['request'] = {'application/json': OpenApiTypes.OBJECT}
        elif isinstance(kwargs.get('request', None),
                            SerializerMetaclass):
            kwargs['request'] = {'application/json': kwargs['request']}
        deco = extend_schema(parameters=parameters,
                             examples=examples if examples else None,
                             responses={
                                 201:
                                 OpenApiResponse(description='???',
                                                 response=response_schema)
                             },
                             **kwargs)
        funcw = deco(func)
        funcw.querys = querys
        funcw.request_body = request_bodys if request_bodys else []
        return funcw

    return myextend_schema


def get_response_serializer(data_serializer=None,msg_list=None,status_msg_keypair=None):
    status_msg_keypair = (
        (
            (201, 'success'),
            'success'
        ),
    ) if status_msg_keypair is None else status_msg_keypair
    msg_list = list(
        set(
            map(
                lambda x: x[1],
                map(
                    lambda x: x[0],
                    status_msg_keypair
                )
            )
        )
    )
    status_list = list(
        set(
            map(
                lambda x: x[0],
                map(
                    lambda x: x[0],
                    status_msg_keypair
                )
            )
        )
    )
    msg_list = ['success'] if msg_list is None else msg_list
    status_list = [201] if status_list is None else status_list
    newclass = type(
        str(uuid.uuid1()),
        (serializers.Serializer, ),
        {
            'status': serializers.IntegerField(
                    default=201,
                    help_text=format_lazy(
                        "{} :" + "{} ; " * len(status_list),
                        *([_("status code")] + status_list)
                    )
                ),
            'msg': serializers.CharField(
                    default='success',
                    help_text=format_lazy(
                        "{} :" + "{} ; " * len(msg_list),
                        *([_("human readable message")] + msg_list)
                    )
                ),
            'data': data_serializer
        }
    )
    return newclass

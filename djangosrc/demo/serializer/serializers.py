from rest_framework import serializers
from demo.utils import get_response_serializer
from django.utils.translation import gettext_lazy as _


class _DocumentArgsSerializer(serializers.Serializer):
    code = serializers.CharField(default=None, help_text=_("Document's corresponding "))
    cmd = serializers.CharField(default=None, help_text=_("Document's corresponding "))
    name = serializers.CharField(default=None, help_text=_("Document's corresponding "))


class _WebSerializer(serializers.Serializer):
    url = serializers.CharField(default="https://www.baidu.com", help_text=_("url传参"))
    content = serializers.CharField(default="null", help_text=_("value"))


class _SqlArgsSerializer(serializers.Serializer):
    # page_size = serializers.IntegerField(default=20, help_text=_('Number per page'))
    # page = serializers.IntegerField(default=1, help_text=_('Page index'))
    sql = serializers.CharField(default=None, help_text=_("Executed SQL statement"))
    name = serializers.CharField(default=None, help_text=_("Document's corresponding "))
    phone1 = serializers.CharField(default=None, help_text=_("Document's corresponding "))
    id = serializers.CharField(default=None, help_text=_("Document's corresponding "))


class _FilePathArgsSerializer(serializers.Serializer):

    name = serializers.CharField(default=None, help_text=_("Document's corresponding "))

_SuccessSerializer = get_response_serializer(serializers.ListField())
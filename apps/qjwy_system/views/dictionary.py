# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
------------------------------------
@Author         :  duanrungang
@Version        :  
@File           :  dictionary.py
@Description    :  
@CreateTime     :  2021/12/14 14:59
@ModifyTime     :  
------------------------------------
"""
from rest_framework import serializers

from apps.qjwy_system.models import Dictionary
from apps.utils.serializer import CustomModelSerializer
from apps.utils.viewset import CustomModelViewSet


class DictionarySerializer(CustomModelSerializer):
    """
    字典-序列化器
    """

    class Meta:
        model = Dictionary
        fields = "__all__"
        read_only_fields = ["id"]


class DictionaryCreateUpdateSerializer(CustomModelSerializer):
    """
    字典管理 创建/更新时的列化器
    """

    class Meta:
        model = Dictionary
        fields = '__all__'


class DictionaryTreeSerializer(CustomModelSerializer):
    """
    字典表的树形序列化器
    """
    children = serializers.SerializerMethodField(read_only=True)

    def get_children(self, instance):
        queryset = Dictionary.objects.filter(parent=instance.id).filter(status=1)
        if queryset:
            serializer = DictionaryTreeSerializer(queryset, many=True)
            return serializer.data
        else:
            return None

    class Meta:
        model = Dictionary
        fields = "__all__"
        read_only_fields = ["id"]


class DictionaryViewSet(CustomModelViewSet):
    """
    字典管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    extra_filter_backends = []
    # permission_classes = []
    search_fields = ['label']
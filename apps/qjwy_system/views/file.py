# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
------------------------------------
@Author         :  duanrungang
@Version        :  
@File           :  file.py
@Description    :  
@CreateTime     :  2021/12/15 14:32
@ModifyTime     :  
------------------------------------
"""
from rest_framework import serializers

from apps.qjwy_system.models import FileList
from apps.utils.serializer import CustomModelSerializer
from apps.utils.viewset import CustomModelViewSet


class FileSerializer(CustomModelSerializer):
    file = serializers.SerializerMethodField(read_only=True)

    def get_file(self, instance):
        return str(instance.url)

    class Meta:
        model = FileList
        fields = "__all__"

    def create(self, validated_data):
        validated_data['fileType'] = str(self.initial_data.get('url')).split('.')[-1]
        validated_data['fileSize'] = round(self.initial_data.get('url').size / 1024 / 1024, 2)
        validated_data['name'] = str(self.initial_data.get('url'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.fileType = str(self.initial_data.get('url')).split('.')[-1]
        instance.fileSize = round(self.initial_data.get('url').size / 1024 / 1024, 2)
        instance.name = str(self.initial_data.get('url'))
        return super().update(instance, validated_data)


class FileViewSet(CustomModelViewSet):
    """
    文件管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = FileList.objects.all()
    serializer_class = FileSerializer
    filter_fields = ['name', ]
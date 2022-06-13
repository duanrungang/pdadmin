# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
------------------------------------
@Author         :  duanrungang
@Version        :  
@File           :  img.py
@Description    :  
@CreateTime     :  2021/12/15 14:32
@ModifyTime     :  
------------------------------------
"""
from rest_framework import serializers

from apps.qjwy_system.models import ImgList
from apps.utils.serializer import CustomModelSerializer
from apps.utils.viewset import CustomModelViewSet


class ImgSerializer(CustomModelSerializer):
    img = serializers.SerializerMethodField(read_only=True)

    def get_img(self, instance):
        return str(instance.url)

    class Meta:
        model = ImgList
        fields = "__all__"

    def create(self, validated_data):
        validated_data['fileType'] = str(self.initial_data.get('url')).split('.')[-1]
        validated_data['fileSize'] = round(self.initial_data.get('url').size / 1024 / 1024, 2)
        validated_data['name'] = str(validated_data.get('url'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.fileType = str(self.initial_data.get('url')).split('.')[-1]
        instance.fileSize = round(self.initial_data.get('url').size / 1024 / 1024, 2)
        instance.name = str(self.initial_data.get('url'))
        return super().update(instance, validated_data)


class ImgViewSet(CustomModelViewSet):
    """
    图片管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = ImgList.objects.all()
    serializer_class = ImgSerializer
    filter_fields = ['name', ]

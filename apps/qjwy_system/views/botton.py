# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
------------------------------------
@Author         :  duanrungang
@Version        :  
@File           :  botton.py
@Description    :  
@CreateTime     :  2021/12/14 14:50
@ModifyTime     :  
------------------------------------
"""
from apps.qjwy_system.models import Button
from apps.utils.serializer import CustomModelSerializer
from apps.utils.viewset import CustomModelViewSet


class ButtonSerializer(CustomModelSerializer):
    """
    按钮权限-序列化器
    """

    class Meta:
        model = Button
        fields = "__all__"
        read_only_fields = ["id"]


class ButtonViewSet(CustomModelViewSet):
    """
    按钮权限接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Button.objects.all()
    serializer_class = ButtonSerializer
    # permission_classes = []

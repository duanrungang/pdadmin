# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
------------------------------------
@Author         :  duanrungang
@Version        :  
@File           :  dept.py
@Description    :  
@CreateTime     :  2021/12/14 14:25
@ModifyTime     :  
------------------------------------
"""
from apps.qjwy_system.models import Dept
from apps.utils.serializer import CustomModelSerializer
from apps.utils.viewset import CustomModelViewSet


class DeptSerializer(CustomModelSerializer):
    """
    部门-序列化器
    """

    class Meta:
        model = Dept
        fields = '__all__'
        read_only_fields = ['id']


class DeptCreateUpdateSerializer(CustomModelSerializer):
    """
    部门管理 创建/更新时的列化器
    """

    class Meta:
        model = Dept
        fields = '__all__'


class DeptViewSet(CustomModelViewSet):
    """
    部门管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Dept.objects.all()
    serializer_class = DeptSerializer
    # permission_classes = []

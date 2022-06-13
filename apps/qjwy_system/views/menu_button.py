# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
------------------------------------
@Author         :  duanrungang
@Version        :  
@File           :  menu_button.py
@Description    :  
@CreateTime     :  2021/12/14 14:51
@ModifyTime     :  
------------------------------------
"""
from apps.qjwy_system.models import MenuButton
from apps.utils.serializer import CustomModelSerializer
from apps.utils.viewset import CustomModelViewSet


class MenuButtonSerializer(CustomModelSerializer):
    """
    菜单按钮-序列化器
    """

    class Meta:
        model = MenuButton
        fields = "__all__"
        read_only_fields = ["id"]


class MenuButtonViewSet(CustomModelViewSet):
    """
    菜单按钮接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = MenuButton.objects.all()
    serializer_class = MenuButtonSerializer
    # permission_classes = []
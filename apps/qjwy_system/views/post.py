# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
------------------------------------
@Author         :  duanrungang
@Version        :  
@File           :  post.py
@Description    :  岗位管理
@CreateTime     :  2022/4/14 08:49
@ModifyTime     :  
------------------------------------
"""
from apps.qjwy_system.models import Post
from apps.utils.serializer import CustomModelSerializer
from apps.utils.viewset import CustomModelViewSet


class PostSerializer(CustomModelSerializer):
    """
    岗位-序列化器
    """

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id']


class PostCreateUpdateSerializer(CustomModelSerializer):
    """
    岗位管理 创建/更新时的列化器
    """

    class Meta:
        model = Post
        fields = '__all__'


class PostViewSet(CustomModelViewSet):
    """
    岗位管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    extra_filter_backends = []
    # permission_classes = []

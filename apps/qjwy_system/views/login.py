# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
------------------------------------
@Author         :  duanrungang
@Version        :  
@File           :  login.py
@Description    :  登陆
@CreateTime     :  2021/12/11 14:58
@ModifyTime     :  
------------------------------------
"""
import base64

from captcha.models import CaptchaStore
from captcha.views import captcha_image
from django.contrib import auth
from django.contrib.auth import login
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.qjwy_system.models import Users
from apps.utils.json_response import ErrorResponse, SuccessResponse
from apps.utils.serializer import CustomModelSerializer


class CaptchaView(APIView):
    """
    验证码
    """
    authentication_classes = []

    @swagger_auto_schema(
        responses={
            '200': openapi.Response('获取成功')
        },
        security=[],
        operation_id='captcha-get',
        operation_description='验证码获取',
    )
    def get(self, request):
        hashkey = CaptchaStore.generate_key()
        id = CaptchaStore.objects.filter(hashkey=hashkey).first().id
        imgage = captcha_image(request, hashkey)
        # 将图片转换为base64
        image_base = base64.b64encode(imgage.content)
        json_data = {"key": id, "image_base": "data:image/png;base64," + image_base.decode('utf-8')}
        return SuccessResponse(data=json_data)


class LoginSerializer(TokenObtainPairSerializer):
    """
    登录序列化器,重写simplejwt序列化器
    """

    class Meta:
        model = Users
        fields = "__all__"
        read_only_fields = ["id"]

    default_error_messages = {
        'no_active_account': _('该账号已被禁用,请联系管理员')
    }

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        user = Users.objects.filter(username=username).first()
        if user and user.check_password(password):
            data = super().validate(attrs)
            refresh = self.get_token(self.user)

            data['name'] = self.user.name
            data['userId'] = self.user.id
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            result = {
                "code": 2000,
                "msg": "请求成功",
                "data": data
            }
        else:
            result = {
                "code": 4000,
                "msg": "账号/密码不正确",
                "data": None
            }
        return result


class LoginView(TokenObtainPairView):
    """
    登陆接口
    """
    serializer_class = LoginSerializer


class ApiLoginSerializer(CustomModelSerializer):
    """接口文档登录-序列化器"""
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = Users
        fields = ['username', 'password']


class ApiLogin(APIView):
    """接口文档的登录接口"""
    serializer_class = ApiLoginSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user_obj = auth.authenticate(request, username=username, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')
        else:
            return ErrorResponse(msg="账号/密码错误")
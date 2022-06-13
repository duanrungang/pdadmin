# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
------------------------------------
@Author         :  duanrungang
@Version        :  
@File           :  exception.py
@Description    :  自定义异常处理
@CreateTime     :  2022/4/13 10:39
@ModifyTime     :  
------------------------------------
"""
import logging
import traceback

from django.db import DatabaseError
from django.db.models import ProtectedError
from rest_framework import exceptions
from rest_framework.exceptions import APIException as DRFAPIException, AuthenticationFailed
from rest_framework.views import set_rollback

from apps.utils.json_response import ErrorResponse

logger = logging.getLogger(__name__)


# 自定义异常处理
def CustomExceptionHandler(exc, context):
    """
    统一异常拦截处理
    目的: 1.取消所有的500异常响应,统一响应为错误返回
          2.准确显示错误信息
    :param exc:
    :param context:
    :return:
    """
    msg = ''
    code = 4000

    if isinstance(exc, AuthenticationFailed):
        code = 401
        msg = exc.detail
    elif isinstance(exc, DRFAPIException):
        set_rollback()
        msg = exc.detail
    elif isinstance(exc, exceptions.APIException):
        set_rollback()
        msg = exc.detail
    elif isinstance(exc, ProtectedError):
        set_rollback()
        msg = "删除失败:该条数据与其他数据有相关绑定"
    elif isinstance(exc, DatabaseError):
        set_rollback()
        msg = "接口服务器异常,请联系管理员"
    elif isinstance(exc, Exception):
        logger.error(traceback.format_exc())
        msg = str(exc)

    # errorMsg = msg
    # for key in errorMsg:
    #     msg = errorMsg[key][0]

    return ErrorResponse(msg=msg, code=code)

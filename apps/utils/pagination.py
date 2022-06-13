# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
------------------------------------
@Author         :  duanrungang
@Version        :  
@File           :  pagination.py
@Description    :  分页设置
@CreateTime     :  2022/4/13 10:48
@ModifyTime     :  
------------------------------------
"""
from collections import OrderedDict

from django.core import paginator
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator as DjangoPaginator
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'
    max_page_size = 999
    django_paginator_class = DjangoPaginator

    def get_paginated_response(self, data):
        code = 2000
        msg = 'success'
        res = {
            "page": int(self.get_page_number(self.request, paginator=paginator)) or 1,
            "total": self.page.paginator.count,
            "limit": int(self.get_page_size(self.request)) or 10,
            "data": data
        }
        if not data:
            code = 2000
            msg = "暂无数据"
            res['data'] = []

        return Response(OrderedDict([
            ('code', code),
            ('msg', msg),
            ('data', res),
        ]))

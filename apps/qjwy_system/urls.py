from django.urls import path, re_path
from rest_framework import routers

from apps.qjwy_system.views.area import AreaViewSet
from apps.qjwy_system.views.botton import ButtonViewSet
from apps.qjwy_system.views.dept import DeptViewSet
from apps.qjwy_system.views.dictionary import DictionaryViewSet
from apps.qjwy_system.views.file import FileViewSet
from apps.qjwy_system.views.img import ImgViewSet
from apps.qjwy_system.views.menu import MenuViewSet
from apps.qjwy_system.views.menu_button import MenuButtonViewSet
from apps.qjwy_system.views.operation_log import OperationLogViewSet
from apps.qjwy_system.views.post import PostViewSet
from apps.qjwy_system.views.role import RoleViewSet
from apps.qjwy_system.views.users import UserViewSet

system_url = routers.SimpleRouter()
system_url.register(r'user', UserViewSet)                       # 用户管理
system_url.register(r'dept', DeptViewSet)                       # 部门管理
system_url.register(r'post', PostViewSet)                       # 岗位管理
system_url.register(r'menu', MenuViewSet)                       # 菜单管理
system_url.register(r'button', ButtonViewSet)                   # 按钮权限管理
system_url.register(r'menu_button', MenuButtonViewSet)          # 菜单按钮管理
system_url.register(r'role', RoleViewSet)                       # 角色管理
system_url.register(r'operation_log', OperationLogViewSet)      # 操作日志接口
system_url.register(r'dictionary', DictionaryViewSet)           # 字典管理
system_url.register(r'area', AreaViewSet)                       # 地区管理
system_url.register(r'img', ImgViewSet)                         # 图片管理
system_url.register(r'file', FileViewSet)                       # 文件管理


urlpatterns = [
    re_path('role/role_id_to_menu/(?P<pk>.*?)/', RoleViewSet.as_view({'get': 'roleId_to_menu'})),   # 通过角色id获取该角色用于的菜单
    path('menu/web_router/', MenuViewSet.as_view({'get': 'web_router'})),                           # 用于前端获取当前角色的路由
    path('user/user_info/', UserViewSet.as_view({'get': 'user_info', 'put': 'update_user_info'})),  # 获取当前用户信息
    re_path('user/change_password/(?P<pk>.*?)/', UserViewSet.as_view({'put': 'change_password'})),  # 密码修改
]
urlpatterns += system_url.urls

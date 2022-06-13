from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView

from application import settings
from apps.qjwy_system.views.login import LoginView, ApiLogin, CaptchaView

schema_view = get_schema_view(
   openapi.Info(
       title="qjwy_loss API",
       default_version='v1',
       description="this is application api documentation",
       terms_of_service="https://www.google.com/policies/terms/",
       contact=openapi.Contact(email="contact@snippets.local"),
       license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/system/', include('apps.qjwy_system.urls')),                                  # 后台管理
    path('api/login/', LoginView.as_view(), name='token_obtain_pair'),                      # 登陆
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),               # 刷新token
    path('apiLogin/', ApiLogin.as_view()),                                                  # 接口文档的登录
    path('api/captcha/', CaptchaView.as_view()),                                            # 验证码

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

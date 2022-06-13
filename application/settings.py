import os
from pathlib import Path
from conf.env import *

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-s-u#af-%vpj2**v-d9@*_@1d!zyx9f1kaki!r9vlga=xtnkx_6'
DEBUG = DEBUG
ALLOWED_HOSTS = ALLOWED_HOSTS


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',                     # 接口文档
    'rest_framework',               # 开发restful接口工具
    'django_filters',               # 过滤器
    'apps.qjwy_system',             # 后台管理模块
    'corsheaders',                  # 跨域
    'captcha',                      # 验证码
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 处理跨域
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.utils.middleware.ApiLoggingMiddleware',
]

# -----------------------------corsheaders start----------------------------
# 全部允许配置
CORS_ORIGIN_ALLOW_ALL = True
# 允许cookie
CORS_ALLOW_CREDENTIALS = True  # 指明在跨域访问中，后端是否支持对cookie的操作
# -----------------------------corsheaders end------------------------------

# -----------------------------djangorestframework start------------
REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",  # 日期时间格式配置
    'DATE_FORMAT': "%Y-%m-%d",
    'DEFAULT_FILTER_BACKENDS': (
        # 'django_filters.rest_framework.DjangoFilterBackend',
        'apps.utils.filters.CustomDjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PAGINATION_CLASS': 'apps.utils.pagination.CustomPagination',  # 自定义分页
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'EXCEPTION_HANDLER': 'apps.utils.exception.CustomExceptionHandler',  # 自定义的异常处理
}
# -----------------------------djangorestframework end--------------

AUTHENTICATION_BACKENDS = [
    'apps.utils.backends.CustomBackend'
]

# 表前缀
TABLE_PREFIX = TABLE_PREFIX
AUTH_USER_MODEL = AUTH_USER_MODEL

# ----------------------------jwt start----------------------------------
from datetime import timedelta

SIMPLE_JWT = {
    # token有效时长
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    # token刷新后的有效时间
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    # 设置前缀
    'AUTH_HEADER_TYPES': ('Bearer',),
    # 'AUTH_HEADER_TYPES': ('JWT',),
    'ROTATE_REFRESH_TOKENS': True
}
# ----------------------------jwt end------------------------------------

# ----------------------------swagger start----------------------------------
SWAGGER_SETTINGS = {
    # 'LOGIN_URL': 'apiLogin/',
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    # 接口文档中方法列表以首字母升序排列
    'APIS_SORTER': 'alpha',
    # 如果支持json提交, 则接口文档中包含json输入框
    'JSON_EDITOR': True,
    # 方法列表字母排序
    'OPERATIONS_SORTER': 'alpha',
    'VALIDATOR_URL': None,
    'AUTO_SCHEMA_TYPE': 2,  # 分组根据url层级分，0、1 或 2 层
    'DEFAULT_AUTO_SCHEMA_CLASS': 'apps.utils.swagger.CustomSwaggerAutoSchema',
}
# ----------------------------swagger end------------------------------------


ROOT_URLCONF = 'application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'application.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'HOST': DATABASE_HOST,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'PORT': DATABASE_PORT,
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
API_LOG_ENABLE = True
# API_LOG_METHODS = 'ALL' # ['POST', 'DELETE']
API_LOG_METHODS = ['POST', 'UPDATE', 'DELETE', 'PUT']  # ['POST', 'DELETE']
API_MODEL_MAP = {
    "/token/": "登录模块",
    "/api/login/": "登录模块",
}

# ----------------log start---------------
SERVER_LOGS_FILE = os.path.join(BASE_DIR, 'logs', 'server.log')
ERROR_LOGS_FILE = os.path.join(BASE_DIR, 'logs', 'error.log')
if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))

# 格式:[2020-04-22 23:33:01][micoservice.apps.ready():16] [INFO] 这是一条日志:
# 格式:[日期][模块.函数名称():行号] [级别] 信息
STANDARD_LOG_FORMAT = '[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s'
CONSOLE_LOG_FORMAT = '[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': STANDARD_LOG_FORMAT
        },
        'console': {
            'format': CONSOLE_LOG_FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'file': {
            'format': CONSOLE_LOG_FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': SERVER_LOGS_FILE,
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 5,  # 最多备份5个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ERROR_LOGS_FILE,
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 3,  # 最多备份3个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        }
    },
    'loggers': {
        # default日志
        '': {
            'handlers': ['console', 'error', 'file'],
            'level': 'INFO',
        },
        'django': {
            'handlers': ['console', 'error', 'file'],
            'level': 'INFO',
        },
        'scripts': {
            'handlers': ['console', 'error', 'file'],
            'level': 'INFO',
        },
        # 数据库相关日志
        'django.db.backends': {
            'handlers': [],
            'propagate': True,
            'level': 'INFO',
        },
    }
}
# ----------------log end-----------------

# ------------------captcha start ---------
CAPTCHA_STATE = True
CAPTCHA_IMAGE_SIZE = (160, 60)  # 设置 captcha 图片大小
CAPTCHA_LENGTH = 4  # 字符个数
CAPTCHA_TIMEOUT = 1  # 超时(minutes)
CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
CAPTCHA_FONT_SIZE = 40  # 字体大小
CAPTCHA_FOREGROUND_COLOR = '#0033FF'  # 前景色
CAPTCHA_BACKGROUND_COLOR = '#F5F7F4'  # 背景色
CAPTCHA_NOISE_FUNCTIONS = (
    'captcha.helpers.noise_arcs',  # 线
    'captcha.helpers.noise_dots',  # 点
)
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge' #字母验证码
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'  # 加减乘除验证码
# ------------------captcha end -----------

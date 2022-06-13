# database setting
# MySQL
DATABASE_ENGINE = 'django.db.backends.mysql'
DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = '3306'
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'gang.818919'
DATABASE_NAME = 'pdadmin'

# other setting
DEBUG = True
ALLOWED_HOSTS = ['*']
TABLE_PREFIX = "qjwy_"
AUTH_USER_MODEL = 'qjwy_system.Users'

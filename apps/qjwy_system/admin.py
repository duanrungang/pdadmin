from django.contrib import admin

# Register your models here.
from apps.qjwy_system.models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'gender', 'email', 'mobile', 'dept')
    list_per_page = 20
    list_select_related = ('dept', )
    list_editable = ('name', )
    search_fields = ('name', 'username',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'sort', 'status')
    list_per_page = 20
    list_editable = ('name', )
    search_fields = ('name',)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'admin', 'key', 'sort', 'status', 'data_range')
    list_per_page = 20
    list_editable = ('name', )
    search_fields = ('name',)


class DeptAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'sort', 'status', 'phone', 'parent')
    list_per_page = 20
    list_editable = ('name', )
    search_fields = ('name',)


class ButtonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')
    list_per_page = 20
    list_editable = ('name', )
    search_fields = ('name',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'icon', 'sort', 'is_link', 'status')
    list_per_page = 20
    list_editable = ('name', )
    search_fields = ('name',)


class MenuButtonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'api', 'method', 'menu')
    list_per_page = 20
    list_editable = ('name', 'api', )
    search_fields = ('name',)


class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('code', 'label', 'value', 'parent', 'status', 'sort')
    list_per_page = 20
    list_editable = ('label', )
    search_fields = ('label',)


class OperationLogAdmin(admin.ModelAdmin):
    list_display = ('request_modular', 'request_path', 'status', 'request_body', 'request_method', 'request_msg', 'request_ip', 'request_browser', 'response_code', 'request_os', 'json_result')
    list_per_page = 20
    # list_editable = ('label', )
    search_fields = ('status',)


class AreaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'level', 'pinyin', 'initials', 'enable', 'pcode')
    list_per_page = 20
    list_editable = ('name', )
    search_fields = ('name',)


class ImgListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'fileType', 'fileClassify', 'fileSize', 'md5sum')
    list_per_page = 20
    list_editable = ('name', )
    search_fields = ('name',)


class FileListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'fileType', 'fileClassify', 'fileSize', 'md5sum')
    list_per_page = 20
    list_editable = ('name', )
    search_fields = ('name',)


admin.site.register(Users, UsersAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Dept, DeptAdmin)
admin.site.register(Button, ButtonAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuButton, MenuButtonAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(OperationLog, OperationLogAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(ImgList, ImgListAdmin)
admin.site.register(FileList, FileListAdmin)
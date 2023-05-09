from django.contrib import admin

# Register your models here.
admin.site.site_title = "数据查重平台"
admin.site.site_header = "数据查重平台"
from django.utils.html import format_html

from .tasks import  forward_msg

from . models import Deduplication

class Deduplication_admin(admin.ModelAdmin):
    list_display = ['taskname', "raw_data", 'comparative_data', 'url', 'status', 'error', 'create_date']
    list_display_links = ['taskname']
    # list_filter = ['hostname',]
    # search_fields = ['hostname', ]
    list_per_page = 10

    def url(self, obj):
        if obj.status is True:
            return format_html('<a  target="_blank" href="/articles/%s/">下载文件</a>' % (obj.id))
        else:
            return format_html('<a  target="_blank">任务执行中</a>')

    # def has_add_permission(self, request):
    #     return  False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_change_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        taskid = forward_msg.delay()
        super().save_model(request, obj, form, change)



admin.site.register(Deduplication, Deduplication_admin)

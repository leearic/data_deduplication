import datetime

from django.db import models

# Create your models here.
import uuid

general = uuid.uuid1()

def user_directory_path(instance, filename):
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d')

    return '{0}/{1}/{2}'.format(nowtime, general, filename)

class Deduplication(models.Model):
    '''
        数据去重
    '''
    taskname = models.CharField(max_length=255, verbose_name="任务名称", help_text='任务名称')
    raw_data = models.FileField(verbose_name="原始数据", help_text='原始数据', upload_to=user_directory_path)
    comparative_data = models.FileField(verbose_name="去重数据", help_text='去重数据', upload_to=user_directory_path)
    status = models.BooleanField(verbose_name="状态", help_text='状态', default=False)
    error = models.BooleanField(verbose_name="错误", help_text='错误', default=False)
    create_date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = u'数据去重'
        verbose_name_plural = u'数据去重'
        ordering = ['-id']

    def __str__(self):
        return '数据去重: 任务名称-' + str(self.taskname)
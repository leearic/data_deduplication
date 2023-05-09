from __future__ import absolute_import, unicode_literals

from bigdata_django.celery import app

from billiard.exceptions import Terminated


@app.task(throws=(Terminated),  soft_time_limit=60, time_limit=60)
def forward_msg():
    print('adgfadfgadfgadfg')
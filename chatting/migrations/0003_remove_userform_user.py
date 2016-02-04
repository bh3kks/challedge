# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0002_auto_20160204_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userform',
            name='user',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0003_remove_userform_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserForm',
            new_name='User',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdb', '0002_auto_20151113_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='scannermoduleresult',
            name='scanner',
            field=models.ForeignKey(default='', to='sdb.Scanner'),
            preserve_default=False,
        ),
    ]

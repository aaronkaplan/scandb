# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import netfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sdb', '0005_auto_20151113_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='ip',
            field=netfields.fields.InetAddressField(unique=True, max_length=39, verbose_name=b'IP address'),
        ),
    ]

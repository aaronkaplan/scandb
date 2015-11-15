# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import netfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sdb', '0004_auto_20151113_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='netblock',
            field=netfields.fields.InetAddressField(default=b'192.168.0.0/24', unique=True, max_length=39, verbose_name=b'Netblock'),
        ),
    ]

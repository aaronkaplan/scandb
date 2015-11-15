# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import netfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sdb', '0003_scannermoduleresult_scanner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='ip',
            field=netfields.fields.InetAddressField(max_length=39, verbose_name=b'IP address'),
        ),
        migrations.AlterField(
            model_name='network',
            name='netblock',
            field=netfields.fields.InetAddressField(default=b'192.168.0.0/24', max_length=39, verbose_name=b'Netblock'),
        ),
    ]

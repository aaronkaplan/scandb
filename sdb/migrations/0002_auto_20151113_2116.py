# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScannerModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=10000, null=True, blank=True)),
                ('url', models.URLField(null=True, verbose_name=b'URL for explanation of the scan module', blank=True)),
                ('scanner', models.ForeignKey(to='sdb.Scanner')),
            ],
        ),
        migrations.CreateModel(
            name='ScannerModuleResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(null=True, verbose_name=b'score', blank=True)),
                ('previous_score', models.FloatField(null=True, verbose_name=b'previous score', blank=True)),
                ('recommendations_url', models.URLField(null=True, verbose_name=b'Link to a site with recommendations on how to improve the situation', blank=True)),
                ('host', models.ForeignKey(to='sdb.Host')),
                ('module', models.ForeignKey(to='sdb.ScannerModule')),
                ('scan', models.ForeignKey(to='sdb.Scan')),
            ],
        ),
        migrations.RemoveField(
            model_name='scanmodule',
            name='scanner',
        ),
        migrations.RemoveField(
            model_name='scanmoduleresult',
            name='host',
        ),
        migrations.RemoveField(
            model_name='scanmoduleresult',
            name='module',
        ),
        migrations.RemoveField(
            model_name='scanmoduleresult',
            name='scan',
        ),
        migrations.DeleteModel(
            name='ScanModule',
        ),
        migrations.DeleteModel(
            name='ScanModuleResult',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField(verbose_name=b'IP address')),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('scannable', models.BooleanField(default=True, verbose_name=b'scannable')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('netblock', models.GenericIPAddressField(default=b'192.168.0.0/24', verbose_name=b'Netblock')),
            ],
        ),
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=10000, null=True, blank=True)),
                ('ts_started', models.DateTimeField(null=True, verbose_name=b'starting time', blank=True)),
                ('ts_finished', models.DateTimeField(null=True, verbose_name=b'finishing time', blank=True)),
                ('continuous', models.NullBooleanField(default=False, verbose_name=b'this scan is continuous?')),
                ('overall_score', models.FloatField(null=True, verbose_name=b'overall score', blank=True)),
                ('authorized_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ScanModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=10000, null=True, blank=True)),
                ('url', models.URLField(null=True, verbose_name=b'URL for explanation of the scan module', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScanModuleResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.FloatField(null=True, verbose_name=b'score', blank=True)),
                ('previous_score', models.FloatField(null=True, verbose_name=b'previous score', blank=True)),
                ('recommendations_url', models.URLField(null=True, verbose_name=b'Link to a site with recommendations on how to improve the situation', blank=True)),
                ('host', models.ForeignKey(to='sdb.Host')),
                ('module', models.ForeignKey(to='sdb.ScanModule')),
                ('scan', models.ForeignKey(to='sdb.Scan')),
            ],
        ),
        migrations.CreateModel(
            name='Scanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(null=True, verbose_name=b'URL describing the scanner', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='scanmodule',
            name='scanner',
            field=models.ForeignKey(to='sdb.Scanner'),
        ),
        migrations.AddField(
            model_name='host',
            name='network',
            field=models.ForeignKey(to='sdb.Network'),
        ),
    ]

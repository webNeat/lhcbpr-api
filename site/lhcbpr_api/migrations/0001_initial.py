# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import lhcbpr_api.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddedResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ApplicationVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=50)),
                ('application', models.ForeignKey(related_name='versions', to='lhcbpr_api.Application', db_index=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AttributeThreshold',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('down_value', models.FloatField()),
                ('up_value', models.FloatField()),
                ('start', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Handler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, db_index=True)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HandlerResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('success', models.BooleanField(default=False)),
                ('handler', models.ForeignKey(to='lhcbpr_api.Handler', db_index=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=50)),
                ('cpu_info', models.CharField(max_length=200)),
                ('memory_info', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
                ('success', models.BooleanField(default=False)),
                ('host', models.ForeignKey(related_name='jobs', null=True, to='lhcbpr_api.Host', db_index=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('application_version', models.ForeignKey(related_name='jobdescriptions', to='lhcbpr_api.ApplicationVersion', db_index=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobHandler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('handler', models.ForeignKey(to='lhcbpr_api.Handler', db_index=False)),
                ('job_description', models.ForeignKey(to='lhcbpr_api.JobDescription', db_index=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobResults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=2000)),
                ('description', models.CharField(max_length=2000)),
                ('is_standalone', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OptionAttribute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('dtype', models.CharField(max_length=8, choices=[(b'str', b'string'), (b'float', b'float'), (b'int', b'integer'), (b'dt', b'datetime')])),
                ('description', models.CharField(max_length=500)),
                ('option', models.ForeignKey(related_name='attributes', to='lhcbpr_api.Option', db_index=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cmtconfig', models.CharField(max_length=100, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RequestedPlatform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cmtconfig', models.ForeignKey(to='lhcbpr_api.Platform', db_index=False)),
                ('job_description', models.ForeignKey(to='lhcbpr_api.JobDescription', db_index=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=lhcbpr_api.models.content_file_name, blank=True)),
                ('job', models.ForeignKey(related_name='files', to='lhcbpr_api.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResultFloat',
            fields=[
                ('jobresults_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lhcbpr_api.JobResults')),
                ('data', models.FloatField()),
            ],
            options={
            },
            bases=('lhcbpr_api.jobresults',),
        ),
        migrations.CreateModel(
            name='ResultInt',
            fields=[
                ('jobresults_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lhcbpr_api.JobResults')),
                ('data', models.IntegerField()),
            ],
            options={
            },
            bases=('lhcbpr_api.jobresults',),
        ),
        migrations.CreateModel(
            name='ResultString',
            fields=[
                ('jobresults_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lhcbpr_api.JobResults')),
                ('data', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=('lhcbpr_api.jobresults',),
        ),
        migrations.CreateModel(
            name='SetupProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='requestedplatform',
            unique_together=set([('job_description', 'cmtconfig')]),
        ),
        migrations.AlterUniqueTogether(
            name='optionattribute',
            unique_together=set([('option', 'name')]),
        ),
        migrations.AddField(
            model_name='jobresults',
            name='job',
            field=models.ForeignKey(related_name='jobresults', to='lhcbpr_api.Job'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobresults',
            name='job_attribute',
            field=models.ForeignKey(related_name='jobresults', to='lhcbpr_api.OptionAttribute', db_index=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='jobhandler',
            unique_together=set([('job_description', 'handler')]),
        ),
        migrations.AddField(
            model_name='jobdescription',
            name='option',
            field=models.ForeignKey(related_name='jobdescriptions', null=True, to='lhcbpr_api.Option', db_index=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='jobdescription',
            name='setup_project',
            field=models.ForeignKey(related_name='jobdescriptions', null=True, to='lhcbpr_api.SetupProject', db_index=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='jobDescription',
            field=models.ForeignKey(related_name='jobs', to='lhcbpr_api.JobDescription'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='platform',
            field=models.ForeignKey(related_name='jobs', to='lhcbpr_api.Platform', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='handlerresult',
            name='job',
            field=models.ForeignKey(to='lhcbpr_api.Job', db_index=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attributethreshold',
            name='attribute',
            field=models.ForeignKey(related_name='thresholds', to='lhcbpr_api.OptionAttribute', db_index=False),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='applicationversion',
            unique_together=set([('application', 'version')]),
        ),
    ]

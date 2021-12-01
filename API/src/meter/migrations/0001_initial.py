# Generated by Django 3.2.9 on 2021-12-01 17:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='meter.Reading.id.helptext', primary_key=True, serialize=False, verbose_name='meter.Reading.id')),
                ('customerId', models.CharField(help_text='meter.Reading.customerId.helptext', max_length=50, verbose_name='meter.Reading.customerId')),
                ('serialNumber', models.CharField(help_text='meter.Reading.serialNumber.helptext', max_length=50, verbose_name='meter.Reading.serialNumber')),
                ('meterType', models.IntegerField(choices=[(0, 'meter.types.electric'), (1, 'meter.types.gas')], default=0, help_text='meter.Reading.meterType.helptext', verbose_name='meter.Reading.meterType')),
                ('meterPointNumber', models.CharField(help_text='meter.Reading.meterPointNumber.helptext', max_length=50, verbose_name='meter.Reading.meterPointNumber')),
                ('readingType', models.CharField(help_text='meter.Reading.readingType.helptext', max_length=20, verbose_name='meter.Reading.readingType')),
                ('registerId', models.CharField(help_text='meter.Reading.registerId.helptext', max_length=20, verbose_name='meter.Reading.registerId')),
                ('value', models.IntegerField(help_text='meter.Reading.value.helptext', verbose_name='meter.Reading.value')),
                ('readDate', models.DateTimeField(auto_now=True, help_text='meter.Reading.readDate.helptext', verbose_name='meter.Reading.readDate')),
                ('parent', models.ForeignKey(blank=True, help_text='meter.Reading.parent.helptext', null=True, on_delete=django.db.models.deletion.CASCADE, to='meter.reading', verbose_name='meter.Reading.parent')),
            ],
            options={
                'verbose_name': 'meter.Reading',
                'verbose_name_plural': 'meter.Readings',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.CharField(help_text='meter.History.id.helptext', max_length=100, primary_key=True, serialize=False, verbose_name='meter.History.id')),
                ('data', models.JSONField(help_text='meter.History.data.helptext', verbose_name='meter.History.data')),
                ('ipaddr', models.CharField(help_text='meter.History.ipaddr.helptext', max_length=40, verbose_name='meter.History.ipaddr')),
                ('date', models.DateTimeField(auto_now=True, help_text='meter.History.date.helptext', verbose_name='meter.History.date')),
                ('stored', models.ForeignKey(blank=True, help_text='meter.History.stored.helptext', null=True, on_delete=django.db.models.deletion.SET_NULL, to='meter.reading', verbose_name='meter.History.stored')),
            ],
            options={
                'verbose_name': 'meter.History',
                'verbose_name_plural': 'meter.Histories',
            },
        ),
    ]

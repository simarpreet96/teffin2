# Generated by Django 2.2.18 on 2021-03-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiffenapp', '0003_auto_20210330_0602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='user',
            name='longitude',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-07 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0004_auto_20200206_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
    ]

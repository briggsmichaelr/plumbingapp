# Generated by Django 3.0.2 on 2020-01-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnose', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='room',
            field=models.CharField(default='foobar', max_length=500),
        ),
        migrations.AlterField(
            model_name='report',
            name='where',
            field=models.CharField(default='foobar', max_length=500),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200211_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address1',
            field=models.CharField(default='NA', max_length=1024),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='address2',
            field=models.CharField(default='NA', max_length=1024),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='city',
            field=models.CharField(default='NA', max_length=1024),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default='NA', max_length=254),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='name',
            field=models.CharField(default='NA', max_length=1024),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='state',
            field=models.CharField(default='NA', max_length=1024),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='zip_code',
            field=models.CharField(default='NA', max_length=12),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-07 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diagnose', '0002_auto_20200126_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(default='NA', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='room',
            field=models.CharField(default='NA', max_length=500),
        ),
        migrations.AlterField(
            model_name='report',
            name='where',
            field=models.CharField(default='NA', max_length=500),
        ),
    ]

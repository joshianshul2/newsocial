# Generated by Django 3.0.8 on 2020-07-26 08:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('socialcustom', '0006_profile1_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile1',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 7, 26, 8, 5, 11, 533793, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile1',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
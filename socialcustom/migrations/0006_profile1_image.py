# Generated by Django 3.0.8 on 2020-07-24 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialcustom', '0005_auto_20200723_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile1',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialcustom', '0007_auto_20200726_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile1',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
# Generated by Django 3.0.8 on 2020-07-23 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialcustom', '0004_auto_20200723_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('address2', models.CharField(max_length=244)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Profile',
            new_name='Profile1',
        ),
    ]

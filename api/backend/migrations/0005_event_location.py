# Generated by Django 3.0.7 on 2020-06-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200627_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
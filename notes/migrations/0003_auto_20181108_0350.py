# Generated by Django 2.1.3 on 2018-11-08 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20181108_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
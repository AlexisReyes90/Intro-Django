# Generated by Django 2.1.3 on 2018-11-14 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dob',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
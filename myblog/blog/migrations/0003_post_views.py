# Generated by Django 2.2.11 on 2020-04-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.BigIntegerField(default=0),
        ),
    ]

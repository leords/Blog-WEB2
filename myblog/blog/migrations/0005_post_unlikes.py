# Generated by Django 2.2.11 on 2020-04-21 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='unlikes',
            field=models.BigIntegerField(default=0),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_auto_20200722_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_liblery',
            name='title',
            field=models.CharField(default='image', max_length=200, verbose_name='Название'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-16 17:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20200716_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Контент'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-07-15 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20200714_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='category_slug',
        ),
    ]

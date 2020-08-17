# Generated by Django 3.0.7 on 2020-08-09 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_auto_20200801_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='mainapp.Category', verbose_name='Категория'),
        ),
    ]
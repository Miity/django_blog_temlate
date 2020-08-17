# Generated by Django 3.0.7 on 2020-08-01 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_post_liblery_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Даиа обновленния'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, default='0', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='mainapp.Category', verbose_name='Категория'),
        ),
    ]
# Generated by Django 3.0.7 on 2020-07-20 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20200717_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Liblery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/image_librery/')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Post')),
            ],
        ),
    ]

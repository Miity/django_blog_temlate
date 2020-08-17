# blog/models.py
from django.db import models
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField

from pilkit.processors import Thumbnail


# Модель категории
class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название')
    parent = models.ManyToManyField('self', blank=True, verbose_name='Категория-родитель', )
    desc = models.TextField("Описание", null=True, blank=True)
    slug = models.SlugField(max_length=255, db_index=True, default='default', unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    post_date = models.DateTimeField("Дата создания", auto_now_add=True)
    update_at = models.DateTimeField('Даиа обновленния', auto_now=True)
    category = models.ForeignKey(Category,
                                 related_name='category',
                                 null=True,
                                 blank=True,
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 default=0,
                                 )
    image = models.ImageField("Главное фото", null=True, blank=True, upload_to='images/')
    image_small = ImageSpecField(source='image',
                                 processors=[Thumbnail(400, 400)],
                                 format='JPEG',
                                 options={'quality': 60})
    title = models.CharField("Название", max_length=200)
    content = RichTextField("Контент", null=True, blank=True)
    excert = models.TextField("Краткое описание", max_length=200, null=True, blank=True)
    slug = models.SlugField(max_length=150, db_index=True, null=True, blank=True, unique=True)
    status = models.BooleanField("Опубликовать?", default=True)
    comment_status = models.BooleanField("Можно комментировать?", default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=(self.slug,), )

    class Meta:
        ordering = ["-post_date", "title"]




class Post_Liblery(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/image_librery/')
    image_small = ImageSpecField(source='image',
                                 processors=[Thumbnail(150, 150)],
                                 format='JPEG',
                                 options={'quality': 60})
    title = models.CharField("Название", max_length=200, default='image')

    def __str__(self):
        return self.post.title


class StaticPage(models.Model):
    title = models.CharField("Название", max_length=200)
    content = RichTextField("Контент", null=True, blank=True)
    status = models.BooleanField("Опубликовать?", default=False)
    menu = models.BooleanField("Выставить в меню?", default=False)
    slug = models.SlugField(max_length=150, db_index=True, null=True, blank=True, unique=True)

    def __str__(self):
        return self.title

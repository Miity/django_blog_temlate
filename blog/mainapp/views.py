import json
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Post, Category, StaticPage, Post_Liblery
from .form import PostForm


class HomeView(TemplateView):
    template_name = "mainapp/index.html"

    def get_context_data(self, *args, **kwargs):
        static_pages = StaticPage.objects.filter(status=True)
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['menu'] = static_pages
        return context


class StaticPageView(DetailView):
    model = StaticPage
    slug_field = "slug"
    template_name = "mainapp/blog/static_page.html"


class CategoryList:
    def get_category(self):
        return Category.objects.all()


class Post_by_Cat(ListView, CategoryList):
    model = Post
    template_name = "mainapp/blog/blog.html"
    ordering = ['-post_date']

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).filter(status=True)


class Post_List(CategoryList, ListView):
    model = Post
    queryset = Post.objects.filter(status=True)
    template_name = "mainapp/blog/partfolio.html"
    ordering = ['-post_date']
    # ordering = ['-id']


class Post_Detail(DetailView):
    model = Post
    slug_field = "slug"

    template_name = "mainapp/blog/post_detail.html"  # указывать не обязательно!, можно через "model", тогда джагнго

    # будет искатьт шаблон Post_detail.html

    def get_context_data(self, *args, **kwargs):
        context = super(Post_Detail, self).get_context_data(*args, **kwargs)
        post = self.object.id
        context['photos'] = Post_Liblery.objects.filter(post=post)
        context['next'] = Post.objects.filter(post_date__gt=self.object.post_date).order_by("post_date").first()
        context['prev'] = Post.objects.filter(post_date__lt=self.object.post_date).order_by("-post_date").first()
        context['ckeditor_config'] = json.dumps(settings.CKEDITOR_CONFIGS["default"])
        return context




# Create Post Admin.

class AddPostView(CreateView):
    model = Post
    template_name = 'mainapp/blog/add_post.html'
    form_class = PostForm
    # fields = '__all__'
    # fields = ('author','category','thumbnail','title','content','slug')

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'mainapp/blog/update_post.html'
    form_class = PostForm

class DeletePostView(DeleteView):
    model = Post
    template_name = 'mainapp/blog/delete_post.html'
    form_class = PostForm
    success_url = reverse_lazy("blog")

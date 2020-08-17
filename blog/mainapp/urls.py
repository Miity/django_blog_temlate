"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import Post_List, Post_Detail, Post_by_Cat, AddPostView, UpdatePostView, DeletePostView,\
    HomeView, StaticPageView
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('<slug:slug>', StaticPageView.as_view(), name='static_page'),
    path('blog/', Post_List.as_view(), name='blog'),
    path('post/<slug:slug>', Post_Detail.as_view(), name = "post_detail" ),
    path('cat/<slug:slug>', Post_by_Cat.as_view(), name = "category"),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('post/update/<slug:slug>', UpdatePostView.as_view(), name = 'update_post'),
    path('post/delete/<slug:slug>', DeletePostView.as_view(), name = 'delete_post'),
]

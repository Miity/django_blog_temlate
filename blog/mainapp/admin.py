# blog/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Category, StaticPage, Post_Liblery



class PostImageAdmin(admin.StackedInline):
    model = Post_Liblery



class PostsInCategory(admin.TabularInline):
    model = Post
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug",)
    list_display_links = ("title",)
    inlines = [PostsInCategory]
    save_on_top = True

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ("id", "title", "category", "status", "post_date", "image")

    fieldsets = (
        ('Параметры', {
            "classes": ("collapse"),
            "fields": (("category", "status"),)
        }),
        ("Пост", {
            "fields": (("title",), ("slug",),("image", "content",))
        }),)

    list_display_links = ("title",)
    search_fields = ("title", "category__title")
    list_editable = ("status",)

    save_as = True

    inlines = [PostImageAdmin]

    class Meta:
        model = Post


admin.site.register(StaticPage)


admin.site.site_title = "Un Viaggio Italiano"
admin.site.site_header = "Un Viaggio Italiano"

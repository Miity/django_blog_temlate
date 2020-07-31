# blog/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Post, Category, StaticPage, Post_Liblery


class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ("id", "title", "category", "status", "post_date")
        export_order = ("id", "title", "category", "status", "post_date")


class BookAdmin(ImportExportModelAdmin):
    resource_class = PostResource

admin.site.register(Post, BookAdmin)

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


class PostAdmin(admin.ModelAdmin):
    resource_class = PostResource
    list_display = ("id", "title", "category", "status", "post_date", "image")

    fieldsets = (
        ('Параметры', {
            "classes": ("collapse"),
            "fields": (("author", "category", "status"),)
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

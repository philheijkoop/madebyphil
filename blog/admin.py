from django.contrib import admin

from .models import Category, Post, Tag

# Register your models here.
admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "publish_date", "published", "category")

admin.site.register(Tag)
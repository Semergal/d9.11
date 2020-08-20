from django.contrib import admin

# Register your models here.
from app.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'content', 'updated', 'publication_date')

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    pass
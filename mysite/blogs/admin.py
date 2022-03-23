from django.contrib import admin

from .models import Blog, Category

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_on')

@admin.register(Category)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name',)

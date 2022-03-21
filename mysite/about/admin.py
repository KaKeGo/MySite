from django.contrib import admin

from .models import About, Skills

# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Skills)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'score')

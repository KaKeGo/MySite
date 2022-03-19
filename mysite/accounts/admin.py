from django.contrib import admin

from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login',)
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff')
    fieldsets = (
        ('Info', {'fields': ('email', 'username', 'password')}),
        ('Personal', {'fields': ('first_name', 'last_name', 'avatar')}),
        ('Permissions', {'fields': ('is_superuser', 'is_admin', 'is_staff', 'is_active')}),
    )

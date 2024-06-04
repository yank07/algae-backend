

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Observation, Request

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'location', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'location', 'role')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'body_of_water', 'algae_level', 'observation_date', 'description')
    list_filter = ('body_of_water', 'observation_date', 'algae_level')
    search_fields = ('body_of_water', 'description')
    ordering = ('-observation_date',)

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('biologist', 'body_of_water', 'request_date', 'description', 'is_fulfilled')
    list_filter = ('body_of_water', 'request_date', 'is_fulfilled')
    search_fields = ('body_of_water', 'description')
    ordering = ('-request_date',)
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone_number', 'is_admin', 'is_staff')
    search_fields = ('email', 'name', 'phone_number')

admin.site.register(CustomUser, CustomUserAdmin)
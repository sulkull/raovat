from typing import List
from django.contrib import admin
from .models import Profile
# Register your models here.


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['username','id', 'email', 'first_name', 'last_name', 'GioiTinh', 'NgaySinh', 'SDT', 'DiaChi']
    search_fields = ['Username']
    list_per_page = 10

admin.site.register(Profile, CustomerUserAdmin)

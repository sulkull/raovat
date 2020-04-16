from typing import List
from django.contrib import admin
from taikhoan.models import *
# Register your models here.


class CustomerUserAdmin(admin.ModelAdmin):
    list_display = ['username','id', 'email', 'first_name', 'last_name', 'GioiTinh', 'NgaySinh', 'SDT', 'DiaChi']
    search_fields = ['Username']
    list_per_page = 10

admin.site.register(Profile, CustomerUserAdmin)

# class PackageUserAdmin(admin.ModelAdmin):
#     list_display = ['ten_goi_vip']
#     list_per_page = 10
#
# admin.site.register(package, PackageUserAdmin)
#
# class VipUserAdmin(admin.ModelAdmin):
#     list_display = ['package','kiemtra']
#     list_per_page = 10
#
# admin.site.register(Vip, VipUserAdmin)
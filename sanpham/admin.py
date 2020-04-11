from django.contrib import admin
# Hiển thị hóa đơn trên trang admin
from sanpham.models import category


class Danhmuc(admin.ModelAdmin):
    list_display = ['title','slug','id']
    list_filter = ['title']
    exclude = ['slug']
    list_per_page = 10
admin.site.register(category, Danhmuc)

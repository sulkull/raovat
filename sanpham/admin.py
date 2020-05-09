from django.contrib import admin
# Hiển thị hóa đơn trên trang admin
from sanpham.models import *


class Danhmuc(admin.ModelAdmin):
    list_display = ['title', 'slug', 'id']
    list_filter = ['title']
    exclude = ['slug']
    list_per_page = 10
admin.site.register(category, Danhmuc)


class Subdanhmuc(admin.ModelAdmin):
    list_display = ['title', 'id']
    list_filter = ['title','category']
    exclude = ['slug']
    list_per_page = 10
admin.site.register(subcategory, Subdanhmuc)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','user','category']
    list_filter = ['title', 'category']
    exclude = ['slug']
    list_per_page = 10
admin.site.register(Post, PostAdmin)

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['post','id']
    list_per_page = 10
    extra = 3
admin.site.register(Images, ImagesAdmin)

class ImageInline(admin.StackedInline):
    model = Images
    extra = 3
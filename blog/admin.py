from django.contrib import admin

# Register your models here.
from blog.models import *


class BlogAd(admin.ModelAdmin):
    list_display = ['tieude', 'slug', 'id']
    list_filter = ['danhmuc']
    exclude = ['slug']
    list_per_page = 10

admin.site.register(Baiviet, BlogAd)

class DanhmucAd(admin.ModelAdmin):
    list_display = ['tieude', 'slug', 'id']
    list_filter = ['tieude']
    exclude = ['slug']
    list_per_page = 10

admin.site.register(Danhmuc, DanhmucAd)
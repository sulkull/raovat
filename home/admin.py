from django.contrib import admin
# Register your models here.
from home.models import *


class Banneradmin(admin.ModelAdmin):
    list_display = ['title','thutu','action']
    search_fields = ['title']
    list_per_page = 10

    save_as = True
admin.site.register(Slider, Banneradmin)

class Ykienkhachhang(admin.ModelAdmin):
    list_display = ['name','action']
    search_fields = ['name']
    list_per_page = 10

    save_as = True
admin.site.register(Ykienkhach, Ykienkhachhang)
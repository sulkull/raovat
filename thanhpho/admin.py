from django.contrib import admin

# Register your models here.
from thanhpho.models import thanhpho, quan_huyen


class ThanhphoAdmin(admin.ModelAdmin):
    list_display = ['title','slug','id']
    list_filter = ['title']
    exclude = ['slug']
    list_per_page = 10
admin.site.register(thanhpho, ThanhphoAdmin)

class QuanhuyenAdmin(admin.ModelAdmin):
    list_display = ['title','slug','id']
    list_filter = ['title',]
    search_fields = ['title',]
    exclude = ['slug']
    list_per_page = 10
admin.site.register(quan_huyen, QuanhuyenAdmin)

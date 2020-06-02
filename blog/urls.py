# Hien thi bai viet - danh muc
from django.urls import path

from blog.views import *

app_name = 'blog'
urlpatterns = [

    path('tin/<str:slug>', XemBaiViet, name='Chi-tiet-tin-tuc'),
    path('danhmuc/<str:slug>', XemDanhMuc, name='Xem-danh-muc-blog'),
]
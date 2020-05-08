from django.conf.urls.static import static
from django.urls import path, re_path
from raovat import settings
from sanpham.views import *

app_name = 'sanpham'
urlpatterns = [

    # quan ly bai viet
    path("quan-ly/dang-bai-viet", post, name='Dang-bai-viet'),
    path("quan-ly/danh-sach-bai", danh_sach_bai, name='Danh-sach-bai'),
    path('quan-ly/sua-bai/<int:id>', post_edit, name='Sua-bai-viet'),
    path('quan-ly/delete/<int:id>', XoaPost.as_view(), name='Xoa-bai-viet'),

    #Hien thi bai viet - danh muc
    path('tin-dang/<str:slug>', XemPost, name='Chi-tiet-bai'),
    path('s/<str:slug>', XemCategory, name='Xem-danh-muc'),

    # trang thai
    path('active/<int:id>', trang_thai_bat, name='Trang-thai-post_active'),
    path('hidden/<int:id>', trang_thai_tat, name='Trang-thai-post_hidden'),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
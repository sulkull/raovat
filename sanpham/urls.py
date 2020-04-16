from django.conf.urls.static import static
from django.urls import path, re_path
from raovat import settings
from sanpham.views import *

app_name = 'sanpham'
urlpatterns = [
    path("dang-bai-viet", post, name='Dang-bai-viet'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
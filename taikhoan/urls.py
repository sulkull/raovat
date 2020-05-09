from django.conf.urls.static import static
from django.urls import path, re_path
from django.conf.urls import url

from raovat import settings
from taikhoan.views import dangki
from . import views
from django.contrib.auth import views as auth_views

app_name = 'taikhoan'
urlpatterns = [
    path("dang-ki", dangki.as_view(), name='dangky'),
    path("dang-nhap", auth_views.LoginView.as_view(template_name='raovat/user/dang-nhap.html'),
         name='dangnhap'),
    path("dang-xuat/", auth_views.LogoutView.as_view(next_page='/'), name='dangxuat'),
    path("thong-tin-tai-khoan/", views.thongtintaikhoan, name='thongtintaikhoan'),
    path("doi-mat-khau/", views.doimatkhau, name='doimatkhau'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

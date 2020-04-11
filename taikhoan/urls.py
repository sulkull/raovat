from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'taikhoan'
urlpatterns = [
    path("dang-ky/", views.dangky, name='dangky'),
    path("dang-nhap", auth_views.LoginView.as_view(template_name='raovat/header.html'),
         name='dangnhap'),
    path("dang-xuat/", auth_views.LogoutView.as_view(next_page='/'), name='dangxuat'),
    path("thong-tin-tai-khoan/", views.thongtintaikhoan, name='thongtintaikhoan'),
    path("doi-mat-khau/", views.doimatkhau, name='doimatkhau'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    path("xac-thuc/", views.verify, name='xacthuc'),
    path("xac-thuc-sdt/", views.checkcode, name='xacthucsdt'),

]

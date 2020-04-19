from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='trang-chu'),
    path('category', views.categorys, name='danh-muc'),
    path('404.html', views.Error404, name='404-error'),
]
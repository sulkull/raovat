from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='trang-chu'),
    path('category', views.category, name='danh-muc'),
]
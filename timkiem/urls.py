from django.urls import path
from timkiem.views import *

app_name='timkiem'
urlpatterns = [
    path('', timkiem, name='tim-kiem'),
]
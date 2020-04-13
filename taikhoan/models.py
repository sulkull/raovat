import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Profile(AbstractUser):
    SDT = models.CharField(default='', max_length=10, verbose_name='Số điện thoại')
    DiaChi = models.TextField(default='', verbose_name='Địa chỉ',null=True)
    choices = [('0', 'Nam'), ('1', 'Nữ'), ('2', 'Không xác định')]
    GioiTinh = models.CharField(choices=choices, default='2', max_length=20, verbose_name='Giới tính')
    NgaySinh = models.DateField(null=True, verbose_name='Ngày sinh')
    avatar = models.ImageField(verbose_name='Hình đại diện', upload_to='media/avatar/%Y/%m/%d/',default='static/images/aditya.png',null=True)

    def HoTen(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = 'Tài khoản'


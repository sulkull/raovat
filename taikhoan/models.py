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

class package(models.Model):
    ten_goi_vip = models.CharField(max_length=100,null=False,verbose_name='Tên gói vip',unique=True)
    def __str__(self):
        return self.ten_goi_vip
    class Meta:
            verbose_name_plural = 'Gói vip'


class Vip(models.Model):
    taikhoan = models.OneToOneField(Profile,on_delete=models.CASCADE,null=False)
    package = models.OneToOneField(package,on_delete=models.CASCADE,null=False,verbose_name='Chọn gói vip')
    ngaytao = models.DateTimeField(auto_now_add=True,auto_created=True,verbose_name='Ngày tạo')
    thoigian = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True,verbose_name ='Chọn thời gian kết thúc')
    kiemtra = models.BooleanField(default=False,verbose_name='Trạng thái')

    class Meta:
        verbose_name_plural = 'Đăng kí Vip'

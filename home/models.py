from django.db import models
from ckeditor.fields import RichTextField

thutu = (
        ('1', 'Đầu tiên'),
        ('2', 'Thứ 2'),
        ('3', 'Thứ 3'),
        ('4', 'Thứ 4'),
        ('5', 'Thứ 5'),
        ('6', 'Thứ 6'),
        ('7', 'Thứ 7')
)
class Slider(models.Model):
    title = models.CharField(max_length=50,null=False,unique=True)
    mota = RichTextField(max_length=1000,verbose_name='Nội dung ',null=True)
    hinh = models.ImageField(upload_to='slider/',verbose_name='Hình slider',null=True)
    thutu = models.CharField(choices=thutu,unique=True,verbose_name='Chọn thứ tự hiện thị',max_length=20,default='2')
    action = models.BooleanField(default=False, verbose_name='Hiện thị ngoài trang chủ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Banner '

class Ykienkhach(models.Model):
    name = models.CharField(max_length=50,null=False)
    mota = RichTextField(max_length=1000,verbose_name='Nội dung ',null=True)
    fb = models.CharField(max_length=90,null=True,default='https://fb.com/#',verbose_name='Link face')
    tw = models.CharField(max_length=90,null=True,default='https://fb.com/#',verbose_name='Link twitter')
    linkedin = models.CharField(max_length=90,null=True,default='https://fb.com/#',verbose_name='linkedin')
    email = models.CharField(max_length=90,null=True,default='abc@gmail.com',verbose_name='email')
    hinh = models.ImageField(upload_to='khach-hang/',verbose_name='Hình đại diện',null=True)
    action = models.BooleanField(default=False, verbose_name='Hiện thị ngoài trang chủ')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Ý kiến khách hàng '
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from raovat.utils import get_unique_slug


class Danhmuc(models.Model):
    tieude = models.CharField(max_length=150,unique=True,null=False,verbose_name='Tiêu đề')
    slug = models.SlugField(max_length=255)
    def __str__(self):
        return  self.tieude

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'tieude', 'slug')
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Danh mục'

class Baiviet(models.Model):
    tieude = models.CharField(max_length=150,unique=True,null=False,verbose_name='Tiêu đề')
    slug = models.SlugField(max_length=255)
    danhmuc = models.ForeignKey(Danhmuc,on_delete=models.Model,verbose_name='Danh mục')
    ngaytao = models.DateField(auto_now_add=True)
    motangan = models.TextField(max_length=300,unique=True,null=False,verbose_name='Mô tả ngắn')
    mota = RichTextField(verbose_name='Mô tả',null=True)
    luotxem = models.IntegerField(default=1)
    hinhanh = models.ImageField(upload_to='media/blog/%Y/%m/%d/',default='/media/media/blog/2020/06/03/hoc-mon-co-gi-choi-trong-nhung-ngay-nang-yen-binh-1.jpg',verbose_name='Hình đại diện')


    def __str__(self):
        return self.tieude
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'tieude', 'slug')
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = 'Tin tức'

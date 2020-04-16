from django.db import models
from django.template.defaultfilters import slugify

from raovat.utils import get_unique_slug
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Tạo danh mục sản phẩm
from taikhoan.models import Profile
from thanhpho.models import *

class subcategory(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Danh mục con'

class category(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)
    slug = models.SlugField(max_length=255)
    subcategory = models.ManyToManyField(subcategory, verbose_name='Chọn danh mục')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Danh mục sản phẩm'


class Post(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False)
    ngaytao = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=100, null=False, unique=True)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(category, on_delete=models.CASCADE, verbose_name='Chọn danh mục')
    subcategory = models.ForeignKey(subcategory,default='', on_delete=models.CASCADE, verbose_name='Chọn danh mục con')
    gia = models.CharField(default='',null=False,max_length=100)
    thanhphos = models.ForeignKey(thanhpho,on_delete=models.CASCADE, verbose_name='Thành phố')
    quan_huyen = models.ForeignKey(quan_huyen,on_delete=models.CASCADE, verbose_name='Quận huyện')
    mota = RichTextField(max_length=1000,verbose_name='Mô tả',null=True)
    diachi = models.CharField(max_length=80,null=True,verbose_name='Địa chỉ')
    action = models.BooleanField(default=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Bài đăng '

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)

class Images(models.Model):
    post = models.ForeignKey(Post, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Hình ảnh')
    class Meta:
        verbose_name_plural = 'Hình ảnh'
from django.db import models

# Create your models here.
# thành phố
from raovat.utils import get_unique_slug

class quan_huyen(models.Model):
    title = models.CharField(max_length=100, null=False,verbose_name='Quận huyện')
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Quận huyện'

class thanhpho(models.Model):
    title = models.CharField(max_length=100, null=False,verbose_name='Thành phố')
    slug = models.SlugField(max_length=255)
    quan_huyen = models.ManyToManyField(quan_huyen, verbose_name='Quận huyện')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Thành phố'
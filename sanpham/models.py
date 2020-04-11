from django.db import models
from raovat.utils import get_unique_slug


# Tạo danh mục sản phẩm
class category(models.Model):
    title = models.CharField(max_length=100, null=False,unique=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Danh mục sản phẩm'

# Generated by Django 3.0.5 on 2020-04-16 07:37

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sanpham.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('thanhpho', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Danh mục sản phẩm',
            },
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Danh mục con',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngaytao', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=255)),
                ('gia', models.CharField(default='', max_length=100)),
                ('mota', ckeditor.fields.RichTextField(max_length=1000, null=True, verbose_name='Mô tả')),
                ('diachi', models.CharField(max_length=80, null=True, verbose_name='Địa chỉ')),
                ('action', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanpham.category', verbose_name='Chọn danh mục')),
                ('quan_huyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thanhpho.quan_huyen', verbose_name='Quận huyện')),
                ('subcategory', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='sanpham.subcategory', verbose_name='Chọn danh mục con')),
                ('thanhphos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thanhpho.thanhpho', verbose_name='Thành phố')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bài đăng ',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=sanpham.models.get_image_filename, verbose_name='Hình ảnh')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sanpham.Post')),
            ],
            options={
                'verbose_name_plural': 'Hình ảnh',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanpham.subcategory', verbose_name='Chọn danh mục'),
        ),
    ]

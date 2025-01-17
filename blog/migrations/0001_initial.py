# Generated by Django 3.0.5 on 2020-06-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Danhmuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieude', models.CharField(max_length=150, unique=True, verbose_name='Tiêu đề')),
                ('slug', models.SlugField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Baiviet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieude', models.CharField(max_length=150, unique=True, verbose_name='Tiêu đề')),
                ('slug', models.SlugField(max_length=255)),
                ('ngaytao', models.DateField(auto_now_add=True)),
                ('motangan', models.TextField(max_length=300, unique=True, verbose_name='Mô tả ngắn')),
                ('mota', models.TextField(unique=True, verbose_name='Mô tả')),
                ('luotxem', models.IntegerField(default=1)),
                ('hinhanh', models.ImageField(default='static/images/aditya.png', upload_to='media/blog/%Y/%m/%d/', verbose_name='Hình đại diện')),
                ('danhmuc', models.ForeignKey(on_delete=models.Model, to='blog.Danhmuc', verbose_name='Danh mục')),
            ],
            options={
                'verbose_name_plural': 'Tin tức',
            },
        ),
    ]

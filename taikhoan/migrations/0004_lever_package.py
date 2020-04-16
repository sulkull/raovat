# Generated by Django 3.0.5 on 2020-04-15 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taikhoan', '0003_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_goi_vip', models.CharField(max_length=100, unique=True, verbose_name='Tên gói vip')),
                ('thoi_gian', models.DateTimeField(max_length=100, verbose_name='Tên gói vip')),
            ],
            options={
                'verbose_name_plural': 'Tài khoản',
            },
        ),
        migrations.CreateModel(
            name='Lever',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taikhoan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Tài khoản',
            },
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanpham', '0003_auto_20200418_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(default='icon/Real-Estate.png', upload_to='icon/', verbose_name='Icon'),
        ),
    ]

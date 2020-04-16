from ckeditor.widgets import CKEditorWidget
from django import forms
from django.utils.translation import gettext

from sanpham.models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category','subcategory','gia','thanhphos','quan_huyen','diachi','mota','action')
        exclude = ('user', 'ngaytao', 'slug','action')
        labels = {
            'title': gettext('Tiêu đề'),
            'category': gettext('Danh mục'),
            'subcategory': gettext('Danh mục con'),
            'gia': gettext('Giá  -  VNĐ'),
            'quan_huyen': gettext('Quận huyện'),
            'mota': gettext('Mô tả'),
            'diachi': gettext('Địa chỉ'),
            'thanhphos': gettext('Thành phố'),
            'action': gettext('Trạng thái '),
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tiêu đề',
                'required': False
            }),
            'mota': CKEditorWidget(attrs={'style':'display: inline-block;'}),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'onchange': 'makeSubmenu(this.value)',
                'required': False
            }),
            'subcategory': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '--------',
                'required': False
            }),
            'gia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nhập giá bán 10000,200000',
                'required': False
            }),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        valid = super(PostForm, self).is_valid()
        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        post = super(PostForm, self).save(commit=False)
        if commit:
            post.save()
        return post


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        exclude = ('post',)

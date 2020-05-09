from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext

from raovat.utils import handler_class_on_validate
from .models import Profile
from django.core.exceptions import ValidationError


# register form
class DangKyForm(UserCreationForm):
    """
    Used by the user to sign up with the website
    """
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Tài khoản', 'label': 'Tài khoản'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    SDT = forms.CharField(max_length=10,
                          widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Số điện thoại'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mật khẩu'}))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Xác nhận mật khẩu'}))

    class Meta:
        model = Profile
        fields = ['username', 'email', 'SDT', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if Profile.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True
        if commit:
            user.save()
        return user


class ThongTinForm(forms.Form):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'style': 'display:none'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    firstname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    choices = [('0', 'Nam'), ('1', 'Nữ'), ('2', 'Không xác định')]
    gioitinh = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={'class': 'form-control'}))
    ngaysinh = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    sdt = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    diachi = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ThongTinForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not Profile.objects.filter(email=email).exclude(id=self.user.id):
            return email
        raise forms.ValidationError("Email đã tồn tại")

    def clean_sdt(self):
        sdt = self.cleaned_data['sdt']
        if not Profile.objects.filter(SDT=sdt).exclude(id=self.user.id):
            return sdt
        raise forms.ValidationError("Số điện thoại đã tồn tại")


class DoiMatKhauForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mật khẩu'}))
    newpassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mật khẩu mới'}))
    renewpassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập lại mật khẩu mới'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DoiMatKhauForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['password']
        if self.user.check_password(password):
            print(password)
            print(self.user.password)
            return password
        raise forms.ValidationError("Mật khẩu không đúng")

    def clean_renewpassword(self):
        if 'newpassword' in self.cleaned_data:
            newpassword = self.cleaned_data['newpassword']
            renewpassword = self.cleaned_data['renewpassword']
            if newpassword == renewpassword and newpassword:
                return renewpassword
            raise forms.ValidationError("Mật khẩu mới không đúng")

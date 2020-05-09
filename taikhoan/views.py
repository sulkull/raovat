from django.conf.global_settings import LOGIN_URL
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from .forms import DangKyForm, ThongTinForm, DoiMatKhauForm
from taikhoan.models import Profile


class dangki(CreateView):
    model = Profile
    form_class = DangKyForm
    template_name = 'raovat/user/dang-ki.html'
    success_url = reverse_lazy('home:trang-chu')

    extra_context = {
        'title': 'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # return HttpResponseRedirect(self.get_success_url())
            return redirect('home:trang-chu')
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password2")
            user.set_password(password)
            user.save()
            return redirect('home:trang-chu')
        else:
            return render(request, 'raovat/user/dang-ki.html', {'form': form})

def thongtintaikhoan(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect('/user/dang-nhap/')


    firstname = user.first_name
    lastname = user.last_name
    email = user.email
    sdt = user.SDT
    diachi = user.DiaChi
    gioitinh = user.GioiTinh
    ngaysinh = user.NgaySinh
    avatar = user.avatar

    data = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'sdt': sdt,
            'diachi': diachi,
            'gioitinh': gioitinh,
            'ngaysinh': ngaysinh,
            'avatar': avatar,
    }

    form = ThongTinForm(initial=data)

    if request.method == 'POST':
        form = ThongTinForm(request.POST,request.FILES, user=request.user)
        #Kiểm tra thông tin
        if form.is_valid():
            if form['email'].value() is not None:
                email = form['email'].value()
            if form['sdt'].value() is not None:
                sdt = form['sdt'].value()
            if form['firstname'].value() is not None:
                firstname = form['firstname'].value()
            if form['lastname'].value() is not None:
                lastname = form['lastname'].value()
            if form['diachi'].value() is not None:
                diachi = form['diachi'].value()
            if form['gioitinh'].value() is not None:
                gioitinh = form['gioitinh'].value()
            if form['ngaysinh'].value() is not None:
                ngaysinh = form['ngaysinh'].value()
            if form['avatar'].value() is not None:
                    avatar = form['avatar'].value()

        user.email = email
        user.SDT = sdt
        user.first_name = firstname
        user.last_name = lastname
        user.DiaChi = diachi
        user.GioiTinh = gioitinh
        user.NgaySinh = ngaysinh
        user.avatar = avatar
        user.save()
    Data = {"User": user,
            "form": form,
            "class" :{'profile':'active'},
            }
    return render(request, 'raovat/user/thong-tin-tai-khoan.html', Data)

def doimatkhau(request):
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect('dang-nhap')
    form = DoiMatKhauForm()

    if request.method == 'POST':
        form = DoiMatKhauForm(request.POST, user=request.user)
        # Kiểm tra thông tin
        if form.is_valid():
            user.set_password(form['renewpassword'].value())
            user.save()
            return HttpResponseRedirect('/tai-khoan/dang-nhap/')

    Data = {"form": form,
            "class":{'pass':'active'}
            }
    return render(request, 'raovat/user/doi-mk.html', Data)

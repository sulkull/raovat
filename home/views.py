from django.db.models.functions import Lower
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from home.models import Slider, thutu, Ykienkhach
from sanpham.models import Post, subcategory, category
from taikhoan.models import Profile
from thanhpho.models import thanhpho


def index(request):
    user = Profile.objects.all()
    cate = subcategory.objects.all()
    danhmuc = category.objects.filter(action=True)
    banner = Slider.objects.filter(action=True).order_by(Lower('thutu').asc())
    ykien = Ykienkhach.objects.filter(action=True)
    tp = thanhpho.objects.all()
    try:
        post = Post.objects.all()
    except Post.DoesNotExist:
        return redirect(reverse_lazy('home:404-error'))
    data = {
        'post':post,
        'user':user,
        'danhmuc':danhmuc,
        'banner':banner,
        'ykien':ykien,
        'cate':cate,
        'tp':tp,
    }
    return render(request, "raovat/index.html",data)

def categorys(request):
    return render(request, "raovat/page/category.html")
def Error404(request):
    return render(request, "raovat/404.html")
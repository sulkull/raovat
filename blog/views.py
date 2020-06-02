from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
# Create your views here.
from django.urls import reverse, reverse_lazy
from blog.models import Baiviet, Danhmuc
from sanpham.models import *

# xem danh muc
def XemDanhMuc(request, slug):
    cate = Danhmuc.objects.get(slug=slug)
    bvm = Baiviet.objects.all()[0:5]
    try:
        post = Baiviet.objects.filter(danhmuc=cate)
        danhmuc = Danhmuc.objects.all()
    except Baiviet.DoesNotExist:
        raise Http404(reverse('home:404-error'))
    ## phan trang
    p = 8
    paginator = Paginator(post, p)
    pageNumber = request.GET.get('page')
    try:
        phantrang = paginator.page(pageNumber)
    except PageNotAnInteger:
        phantrang = paginator.page(1)
    except EmptyPage:
        phantrang = paginator.page(paginator.num_pages)
    data = {
        'post':post,
        'cate':cate,
        'bvm':bvm,
        'danhmuc':danhmuc,
        'phantrang':phantrang,
        }
    return render(request, 'raovat/page/list-danh-muc-blog.html', data)


def XemBaiViet(request, slug):
    danhmuc = Danhmuc.objects.all()
    bvm = Baiviet.objects.all()[0:5]
    try:
        post = Baiviet.objects.get(slug=slug)
    except Baiviet.DoesNotExist:
        raise Http404(reverse('home:404-error'))
    post.luotxem += 1
    post.save()
    data = {
        'post':post,
        'danhmuc':danhmuc,
        'bvm':bvm,
        }
    return render(request, 'raovat/page/tin-tuc.html', data)
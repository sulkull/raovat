from django.db.models import Q
from django.shortcuts import render

from sanpham.models import Post, category
from thanhpho.models import thanhpho

def timkiem(request):
    post = Post.objects.all()
    tp = thanhpho.objects.all()
    cate = category.objects.all()

    tukhoa = request.GET.get('tukhoa')
    if tukhoa:
        post = post.filter(
            Q(title__contains=tukhoa) | Q(mota__contains=tukhoa)
        )
    thanhphos = request.GET.get('tp')
    if thanhphos:
        post = post.filter(
            Q(thanhphos__in=thanhphos)
        )

    danhmuc = request.GET.get('dm')
    if danhmuc:
        post = post.filter(
            Q(category__in=danhmuc)
        )

    data ={
        'post':post,
        'tukhoa':tukhoa,
        "phantrang":post,
        "tp": tp,
        "danhmuc":cate,
        }
    return render(request, 'raovat/page/ket-qua-tim-kiem.html',data)
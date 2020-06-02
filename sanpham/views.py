from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import DeleteView

from sanpham.forms import ImageForm, PostForm
from sanpham.models import *


@login_required(login_url='tai-khoan/dang-nhap')
def post(request):
    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=3)
    # 'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(post=post_form, image=image)
                    photo.save()
            messages.success(request,
                             "Upload thành công!")
            return redirect(reverse_lazy('sanpham:Danh-sach-bai'))
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    cate = category.objects.all()
    tp = thanhpho.objects.all()
    data = {'cate': cate,
            'tp': tp,
            'f': postForm,
            'hinh': formset,
            }
    return render(request, 'raovat/post/dang-bai.html',
                  data)


# Sua bai viet
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3, max_num=3)
    # 'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        form = PostForm(request.POST or None, instance=post)
        formset = ImageFormSet(request.POST or None, request.FILES or None)

        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            print(formset.cleaned_data)
            data = Images.objects.filter(post=post)

            for index, f in enumerate(formset):
                if f.cleaned_data:
                    if f.cleaned_data['id'] is None:
                        photo = Images(post=post, image=f.cleaned_data.get('image'))
                        photo.save()
                    elif f.cleaned_data['image'] is False:
                        photo = Images.objects.get(id=request.POST.get('form-' + str(index) + '-id'))
                        photo.delete()

                    else:
                        photo = Images(post=post, image=f.cleaned_data.get('image'))
                        d = Images.objects.get(id=data[index].id)
                        d.image = photo.image
                        d.save()

            return redirect(reverse_lazy('sanpham:Danh-sach-bai'))
        else:
            print(form.errors, formset.errors)
    else:
        form = PostForm(instance=post)
        formset = ImageFormSet(queryset=Images.objects.filter(post=post))
    cate = category.objects.all()
    tp = thanhpho.objects.all()
    data = {'cate': cate,
            'tp': tp,
            'f': form,
            'hinh': formset,
            }
    return render(request, 'raovat/post/dang-bai.html',
                  data)


@login_required(login_url='tai-khoan/dang-nhap')
def danh_sach_bai(request):
    user = request.user
    pub = Post.objects.filter(action=True)
    hiden = Post.objects.filter(action=False)
    try:
        post = Post.objects.filter(user=user)
    except Post.DoesNotExist:
        return redirect(reverse_lazy('home:404-error'))
    ## phan trang
    p = 5
    paginator = Paginator(post, p)
    pageNumber = request.GET.get('page')
    try:
        phantrang = paginator.page(pageNumber)
    except PageNotAnInteger:
        phantrang = paginator.page(1)
    except EmptyPage:
        phantrang = paginator.page(paginator.num_pages)

    data = {
        'post': post,
        'pub': pub,
        'hiden': hiden,
        'phantrang': phantrang,
        'class': {
            'post': 'active'
        }
    }
    return render(request, 'raovat/post/danh-sach-bai.html',
                  data)


@login_required(login_url='tai-khoan/dang-nhap')
def trang_thai_bat(request, id=None):
    # bật
    a = Post.objects.get(user_id=request.user.id, id=id)
    a.action = True
    a.save()
    return HttpResponseRedirect(reverse_lazy('sanpham:Danh-sach-bai'))


@login_required(login_url='tai-khoan/dang-nhap')
def trang_thai_tat(request, id=None):
    # tắt
    a = Post.objects.get(user_id=request.user.id, id=id)
    a.action = False
    a.save()
    return HttpResponseRedirect(reverse_lazy('sanpham:Danh-sach-bai'))


# xoa bai viet
class XoaPost(DeleteView):
    template_name = 'raovat/post/delete-post.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def get_success_url(self):
        return reverse('sanpham:Danh-sach-bai')
# xem bai viet
def XemPost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404(reverse('home:404-error'))
    post_lien_quan = Post.objects.filter(category=post.category,action=True).order_by('?')
    post_lien_quan_tp = Post.objects.filter(category=post.category,thanhphos=post.thanhphos, action=True)
    post.luotxem += 1
    post.save()
    data = {
        'post':post,
        'plq':post_lien_quan,
        'p_tp':post_lien_quan_tp,
        }
    return render(request, 'raovat/page/detail-page.html', data)

# xem danh muc
def XemCategory(request, slug):
    cate = category.objects.get(slug=slug)
    try:
        post = Post.objects.filter(category=cate)
        danhmuc = category.objects.all()
        tp = thanhpho.objects.all()
    except Post.DoesNotExist:
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
        'danhmuc':danhmuc,
        'tp':tp,
        'phantrang':phantrang,
        }
    return render(request, 'raovat/page/list-danh-muc.html', data)
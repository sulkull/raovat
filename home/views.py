from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "raovat/index.html")
def category(request):
    return render(request, "raovat/page/category.html")
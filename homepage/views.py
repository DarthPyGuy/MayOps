from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'homepage/home.html')


def blog(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Blog'
    }
    return render(request, 'homepage/blog.html', context)


def about(request):
    return render(request, 'homepage/about.html', {'title': 'About Me'})

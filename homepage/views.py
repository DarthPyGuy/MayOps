from django.shortcuts import render

def home(request):
    return render(request, 'homepage/home.html')

def blog(request):
    return render(request, 'homepage/blog.html')

def about(request):
    return render(request, 'homepage/about.html')

from django.shortcuts import render

posts = [
    {
        'author': 'John May',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 29, 2020'
    },
     {
        'author': "John May",
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Tbd 00, 2020'
    }
]

def home(request):
    return render(request, 'homepage/home.html')

def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'homepage/blog.html', context)

def about(request):
    return render(request, 'homepage/about.html')

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>MayOps</h1>")

def blog(request):
    return HttpResponse("<h1>Blog</h1>")

def about(request):
    return HttpResponse("<h1>About Me</h1>")

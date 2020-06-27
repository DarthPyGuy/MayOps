from django.shortcuts import render
from django.http import httpResponse

def home(request):
    return httpResponse("<h1>MayOps</h1>")

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('blog/', views.blog, name="blog"),
    path('about/', views.about, name="about"),
]

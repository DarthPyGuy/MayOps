from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="MayOps-home"),
    path('blog/', views.blog, name="MayOps-blog"),
    path('about/', views.about, name="MayOps-about"),
]

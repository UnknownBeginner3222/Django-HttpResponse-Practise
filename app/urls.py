from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name="home"),
    path("blog", views.blog, name="blog"),
    path("services",views.services,name="services"),
    path("contact",views.contact,name="conatat"),
    path("about",views.about,name="about")
]

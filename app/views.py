from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is home pages <a href='https://www.shrestharakesh.com.np/'> Vist Me </a>")

def about(request):
    return HttpResponse("This is about page <a href='https://www.shrestharakesh.com.np/'> Vist Me </a>")

def contact(request):
    return HttpResponse("This is contact pages <a href='https://www.shrestharakesh.com.np/'> Vist Me </a>")

def services(request):
    return HttpResponse("This is services pages <a href='https://www.shrestharakesh.com.np/'> Vist Me </a>")

def blog(request):
    return HttpResponse("This is Blog Pages <a href='https://www.shrestharakesh.com.np/'> Vist Me </a>")




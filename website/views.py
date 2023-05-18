from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse('<h2>Home page<h2>')

def about_view(request):
    return HttpResponse('<h2>About page<h2>')

def contact_view(request):
    return HttpResponse('<h2>Contact page<h2>')
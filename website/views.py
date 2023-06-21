from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from blog.models import Post

def index_view(request):
    posts = Post.objects.all().order_by('-created_date')
    context = {'posts':posts}
    return render(request, 'website/index.html', context)


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    return render(request, 'website/contact.html')
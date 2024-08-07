from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from blog.models import Post
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsletterForm
from django.contrib import messages
def index_view(request):
    posts = Post.objects.all().order_by('-created_date')
    context = {'posts':posts}
    return render(request, 'website/index.html', context)



def about_view(request):
    return render(request, 'website/about.html')



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'تیکت شما با موفقیت ثبت شد')
        else:
            messages.add_message(request,messages.ERROR,'خطا در انجام عملیات')
    form = ContactForm()
    return render(request, 'website/contact.html',{'form':form})



def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')




def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')

    form = ContactForm()

    return render(request,'test.html',{'form':form})


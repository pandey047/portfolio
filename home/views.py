from django.shortcuts import render,redirect
from .models import Contact,Blog
from .forms import ContactForm
import math
# Create your views here.
def home(request):
    return render(request,'home.html')

def python(request):
    return render(request,'python.html')

def java(request):
    return render(request,'java.html')

def blog(request):
    blog=Blog.objects.all().order_by('-time')
    
    '''
    no_of_posts=4
    page=request.GET.get('page')
    if page is None:
        page=1
    else:
        page=int(page)
    blog=Blog.objects.all().order_by('-time')[(page-1)*no_of_posts:page*no_of_posts]
    length=len(blog)
    if page>1:
        prev=page-1
    else:
        prev=None
    
    if page<math.ceil(length/no_of_posts):
        nxt=page+1
    else:
        nxt=None
    '''
    return render(request,'blog.html',{'blog':blog})

def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first()
    return render(request,'blogpost.html',{'blog':blog})
'''
def contact(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return home(request)
        

    return render(request,'contact.html',{'form':form})

'''
def search_view(request):
      if request.method == 'GET':  
          search_text = request.GET.get("search_box", None)
          records=Contact.objects.filter(columnn__contains=search_text)     
          from django.http import JsonResponse
          return JsonResponse({"result_records":records})


def embeddedHardware(request):
    return render(request,'embeddedhardware.html')


def embeddedFirmware(request):
    return render(request,'embeddedfirmware.html')
from django.shortcuts import render,redirect
from .models import Contact
from .forms import ContactForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def project(request):
    return render(request,'project.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return home(request)
        

    return render(request,'contact.html',{'form':form})


def search_view(request):
      if request.method == 'GET':  
          search_text = request.GET.get("search_box", None)
          records=Contact.objects.filter(columnn__contains=search_text)     
          from django.http import JsonResponse
          return JsonResponse({"result_records":records})
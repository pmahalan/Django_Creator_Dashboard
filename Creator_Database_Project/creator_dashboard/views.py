from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatorForm

# Create your views here.
from .models import *

def home(request):
    creators = Creator.objects.all()
    return render(request, 'accounts/dashboard.html', {'creators': creators})




def formPage(request):
    # vuln = get_object_or_404(Vuln, pk=pk)
    if request.method == "POST":
        r_form = CreatorForm(request.POST, request.FILES)
        print(request.FILES)
        print(request)
        if r_form.is_valid():
            Creator.objects.all().delete()
            view_form = r_form.save(commit=False)
            view_form.save()
            return redirect("home")
        else: 
            print("this is not valid")
    else:
        r_form = CreatorForm()
    context = dict(form=r_form)
    template = 'accounts/newTemplate.html'
    return render(request, template, context)

# def changeName(request):
#     context = {}
#     return render(request, 'accounts/dashboard.html', context)
    

# def uploadPic(request):
#     context = {}
#     return render(request, 'accounts/dashboard.html', context)
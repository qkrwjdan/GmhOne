from django.shortcuts import render,redirect
from .forms import SignUpForm,UploadFileForm
from .models import  UploadFile

# Create your views here.

def ViewOnRoad_index(request):
    return render(request,'ViewOnRoad/ViewOnRoad_index.html',{})


def ViewOnRoad_signup(request):
    form = SignUpForm()
    return render(request,'ViewOnRoad/ViewOnRoad_signup.html',{
        'form':form,
    })


def ViewOnRoad_notice(request):
    return render(request,'ViewOnRoad/ViewOnRoad_notice.html',{})


def ViewOnRoad_fileUpload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect("ViewOnRoad_longWay")
    else:
        form = UploadFileForm() 
    return render(request,'ViewOnRoad/ViewOnRoad_fileUpload.html',{
        'form':form
    })

def ViewOnRoad_longWay(request):
    qs =  UploadFile.objects.all()
    qs =  qs.order_by('-title')
    
    return render(request,'ViewOnRoad/ViewOnRoad_longWay.html',{
        'filelist': qs,
    })

def ViewOnRoad_signin(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST,request.FILES)
        if form.is_valid():
            return redirect('ViewOnRoad_index')
    else:
        form = SignUpForm()
    
    return render(request,'ViewOnRoad/ViewOnRoad_signin.html',{
        'form' : form,
    })
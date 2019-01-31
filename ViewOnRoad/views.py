from django.shortcuts import render
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
    form = UploadFileForm() 
    return render(request,'ViewOnRoad/ViewOnRoad_fileUpload.html',{
        'form':form
    })

def ViewOnRoad_longWay(request):
    qs =  UploadFile.objects.all()
    qs =  UploadFile.order_by('-title')
    
    return render(request,'ViewOnRoad/ViewOnRoad_longWay.html',{
        'filelist': qs,
    })
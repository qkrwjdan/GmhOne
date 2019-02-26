from django.shortcuts import render,redirect,get_object_or_404
from .forms import longway_UploadFileForm,storyonroad_uploadFileForm,roadview_uploadFileForm
from .models import longway_uploadFile_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def ViewOnRoad_index(request):
    return render(request,'ViewOnRoad/ViewOnRoad_index.html',{})

def ViewOnRoad_signup1(request):
    return render(request,'ViewOnRoad/Partner/ViewOnRoad_signup1.html',{})

def ViewOnRoad_signup2(request):
    return render(request,'ViewOnRoad/Partner/ViewOnRoad_signup2.html')

def ViewOnRoad_signup4(request):
    return render(request,'ViewOnRoad/Partner/ViewOnRoad_signup4.html')

def ViewOnRoad_notice(request):
    return render(request,'ViewOnRoad/ViewOnRoad_notice.html',{})

@login_required
def ViewOnRoad_fileupload(request,pk):
    if pk == "1":
        if request.method == "POST":
           form = storyonroad_uploadFileForm(request.POST,request.FILES)
           if form.is_valid:
                form.save()
                return redirect("ViewOnRoad_storyonroad")
        else:
            form = storyonroad_uploadFileForm()
        return render(request,"ViewOnRoad/ViewOnRoad_fileUpload.html",{
            "form":form , "pk":pk
        })
    elif pk == "2":
        if request.method == "POST":
            form = longway_UploadFileForm(request.POST,request.FILES)
            if form.is_valid:
                form.save()
                return redirect("ViewOnRoad_longWay")
        else:
            form = longway_UploadFileForm()
        return render(request,'ViewOnRoad/ViewOnRoad_fileUpload.html',{
            "form":form , "pk":pk
        })
    elif pk == "3":
        if request.method == "POST":
            form = roadview_uploadFileForm(request.POST,request.FILES)
            if form.is_valid:
                form.save()
                return redirect("ViewOnRoad_roadview")
        else:
            form = roadview_uploadFileForm() 
        return render(request,"ViewOnRoad/ViewOnRoad_fileUpload.html",{
            "form":form , "pk":pk
        })


def ViewOnRoad_longWay(request):
    qs = longway_uploadFile_model.objects.all()
    qs = qs.order_by('title')
    
    return render(request,'ViewOnRoad/ViewOnRoad_longWay.html',{
        'filelist': qs,
    })

def ViewOnRoad_storyonroad(request):

    return render(request,'ViewOnRoad/ViewOnRoad_storyonroad.html',{})

def ViewOnRoad_roadview(request):
    return render(request,'ViewOnRoad/ViewOnRoad_roadview.html',
    {

    })

def ViewOnRoad_detail(request,pk):
    qs = get_object_or_404(longway_uploadFile_model,pk=pk)

    return render(request,'ViewOnRoad/ViewOnRoad_detail.html',{
        "file" : qs,
    })

def ViewOnRoad_profile(request):
    if request.user.is_authenticated:
        data = {'username':request.user.username, 'password':request.user.password,
         'last_login':request.user.last_login}
    else:
        data = {'username':requset.user, 'is_authenticated':request.user.is_authenticated}
    return render(request, 'ViewOnRoad/ViewOnRoad_profile.html', context={'data':data})

def UserCreateView(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
 
    else:
        f = UserCreationForm()
 
    return render(request, 'ViewOnRoad/Partner/ViewOnRoad_signup3.html', {'form': f})
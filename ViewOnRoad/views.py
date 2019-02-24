from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm,UploadFileForm,longWay_UploadFileForm
from .forms import storyonroad_uploadFileForm,roadview_uploadFileForm
from .models import  UploadFile
from django.contrib.auth.decorators import login_required

# Create your views here.

def ViewOnRoad_index(request):
    return render(request,'ViewOnRoad/ViewOnRoad_index.html',{})

def ViewOnRoad_signup1(request):
    return render(request,'ViewOnRoad/Partner/ViewOnRoad_signup1.html',{})

def ViewOnRoad_signup2(request):
    return render(request,'ViewOnRoad/Partner/ViewOnRoad_signup2.html')

def ViewOnRoad_signup3(request):
    return render(request,'ViewOnRoad/Partner/ViewOnRoad_signup3.html')

def ViewOnRoad_signup4(request):
    return render(request,'ViewOnRoad/Partner/ViewOnRoad_signup4.html')

def ViewOnRoad_notice(request):
    return render(request,'ViewOnRoad/ViewOnRoad_notice.html',{})

@login_required
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

def ViewOnRoad_fileuploadtest(request,pk):
    if pk == "1":
        if request.method == "POST":
           form = storyonroad_uploadFileForm(request.POST,request.FILES)
           if form.is_valid:
                form.save()
                return redirect("ViewOnRoad_storyonroad")
        else:
            form = storyonroad_uploadFileForm()
        return render(request,"ViewOnRoad/ViewOnRoad_fileUploadtest.html",{
            "form":form , "pk":pk
        })
    elif pk == "2":
        if request.method == "POST":
            form = longWay_UploadFileForm(request.POST,request.FILES)
            if form.is_vaild:
                form.save()
                return redirect("ViewOnRoad_longWay")
        else:
            form = longWay_UploadFileForm()
        return render(request,'ViewOnRoad/ViewOnRoad_fileUploadtest.html',{
            "form":form , "pk":pk
        })
    elif pk == "3":
        if request.method == "POST":
            form = roadview_uploadFileForm(request.POST,request.FILES)
            if form.is_valid:
                form.save()
                return redirect("ViewOnRoad_storyonroad")
        else:
            form = roadview_uploadFileForm() 
        return render(request,"ViewOnRoad/ViewOnRoad_fileUploadtest.html",{
            "form":form , "pk":pk
        })


def ViewOnRoad_longWay(request):
    qs =  UploadFile.objects.all()
    qs =  qs.order_by('title')
    
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
    qs = get_object_or_404(UploadFile,pk=pk)

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
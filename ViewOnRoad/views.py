from django.shortcuts import render,redirect,get_object_or_404
from .forms import longway_UploadFileForm,storyonroad_uploadFileForm,roadview_uploadFileForm,question_Form
from .models import longway_uploadFile_model,storyonroad_uploadFile_model,roadview_uploadFile_model,question_model
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
    if request.user.is_authenticated:
        data = {'ID':request.user.username, '최근 로그인':request.user.last_login}
    else:
        data = {'ID':requset.user, '로그인 여부':request.user.is_authenticated}
    return render(request, 'ViewOnRoad/Partner/ViewOnRoad_signup4.html', context={'data':data})

@login_required
def ViewOnRoad_ask(request):
    if request.method == "POST":
        form = question_Form(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect("ViewOnRoad_questions")
    else:
        form = question_Form()
    return render(request,"ViewOnRoad/Partner/ViewOnRoad_ask.html",{
        "form" : form
    })

def ViewOnRoad_questions(request):
    qs = question_model.objects.all()
    qs = qs.order_by("created_date")

    return render(request,'ViewOnRoad/Partner/ViewOnRoad_questions.html',{
        "posts" : qs,
    })

def ViewOnRoad_question_detail(request,pk):
    post = get_object_or_404(question_model,pk=pk)
    return render(request,"ViewOnRoad/Partner/ViewOnRoad_question_detail.html",{
        "file" : post
        })

@login_required
def ViewOnRoad_profile(request):
    if request.user.is_authenticated:
        data = {'ID':request.user.username, '최근 로그인':request.user.last_login}
    else:
        data = {'ID':requset.user, '로그인 여부':request.user.is_authenticated}
    return render(request, 'ViewOnRoad/ViewOnRoad_profile.html', context={'data':data})

def ViewOnRoad_notice(request):
    return render(request,'ViewOnRoad/ViewOnRoad_notice.html',{})

@login_required
def ViewOnRoad_fileupload(request,pk):
    if pk == "1":
        if request.method == "POST":
           form = storyonroad_uploadFileForm(request.POST,request.FILES)
           if form.is_valid:
                post = form.save()
                # post.author = request.user
                # post.save()
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
                post = form.save()
                # post.author = request.user
                # post.save()
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
                post = form.save()
                # post.author = request.user
                # post.save()
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

def ViewOnRoad_longway_detail(request,pk):
    qs = get_object_or_404(longway_uploadFile_model,pk=pk)
    qs.views += 1
    qs.save()
    return render(request,'ViewOnRoad/ViewOnRoad_detail.html',{
        "file" : qs, 
    })
def ViewOnRoad_storyonroad(request):
    qs = storyonroad_uploadFile_model.objects.all()
    qs = qs.order_by('title')

    return render(request,'ViewOnRoad/ViewOnRoad_storyonroad.html',{
        'filelist' : qs,
    })

def ViewOnRoad_storyonroad_detail(request,pk):
    qs = get_object_or_404(storyonroad_uploadFile_model,pk=pk)
    qs.views += 1
    qs.save()
    return render(request,'ViewOnRoad/ViewOnRoad_detail.html',{
        "file" : qs,
    })
def ViewOnRoad_roadview(request):
    qs = roadview_uploadFile_model.objects.all()
    qs = qs.order_by('title')

    return render(request,'ViewOnRoad/ViewOnRoad_roadview.html',{
        'filelist' : qs,
    })
def ViewOnRoad_roadview_detail(request,pk):
    qs = get_object_or_404(roadview_uploadFile_model,pk=pk)
    qs.views +=1
    qs.save()
    return render(request,"ViewOnRoad/ViewOnRoad_detail.html",{
        "file" : qs,
    })
    


def UserCreateView(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return render(request,'ViewOnRoad/Partner/ViewOnRoad_signup4.html')
 
    else:
        f = UserCreationForm()
 
    return render(request, 'ViewOnRoad/Partner/ViewOnRoad_signup3.html', {'form': f})
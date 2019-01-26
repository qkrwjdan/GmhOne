from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.

def ViewOnRoad_index(request):
    return render(request,'ViewOnRoad/ViewOnRoad_index.html',{})


def ViewOnRoad_signup(request):
    form = SignUpForm()
    return render(request,'ViewOnRoad/ViewOnRoad_signup.html',{
        'form':form,
    })
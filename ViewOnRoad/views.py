from django.shortcuts import render

# Create your views here.

def ViewOnRoad_index(request):
    return render(request,'ViewOnRoad/ViewOnRoad_index.html',{})
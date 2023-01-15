
from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import User
from .forms import Crudform
# Create your views here.


def addandshow(request):
    if request.method == "POST":
        fm = Crudform(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = Crudform()
    data = User.objects.all()
    return render(request, 'addandshow.html', {'form' : fm, 'dta': data})

def update(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Crudform(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('/')
    else:
        pi = User.objects.get(pk=id)
        fm = Crudform(instance=pi)
    return render(request, 'update.html',{'form':fm})

def delete(request, id):
    if request.method == "POST":
        dl = User.objects.get(pk = id)
        dl.delete()
    return HttpResponseRedirect('/')

    

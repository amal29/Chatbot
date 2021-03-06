from django.shortcuts import render,redirect
import datetime 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from.models import *



def Register(request):
   
    form=CreateUserForm()
    print(form)
    
    if request.method=='POST':
        pass1=request.POST["password"]
        pass2=request.POST["password2"]
        if pass1 != pass2:
            messages.warning(request,'Password is Incorrect')
        else:
            form=CreateUserForm(request.POST)
            if form.is_valid():
                 form.save()
            # user=form.cleaned_data.get('username')
            # messages.success(request,'Account was created for ' +  user)
            return redirect('login')
    context={'form':form}
           
    return render(request,'registration.html',context)





def Login(request):
    if request.method=='POST':
        username=  request.POST.get('name')
        print('username:',username)
        password= request.POST.get('password')
        if UserData.objects.filter(name=username,password=password) :
            return HttpResponse("<script>alert('Welcome user');window.location.href='/show'</script>")

        else:
            messages.warning(request,"Username or Password is Incorrect")    
    return render(request,"login.html")



 
def Logout(request):
    logout(request)
    return redirect('login')
   
def Show(request):
    return render(request,'dashboard.html')  
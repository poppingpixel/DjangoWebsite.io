
from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

def home(request):
    return render(request,'home.html')

def handlesignup(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Email = request.POST['Email']
        Pass1= request.POST['Pass1']
        Pass2= request.POST['Pass2']
        
        
        if User.objects.filter(username=Username).exists():
            messages.error(request,"Username Taken")
            return redirect('home')
        elif User.objects.filter(email=Email).exists():
            messages.error(request,"Email taken")
            return redirect('home')
        elif Pass1 != Pass2:
            messages.error(request,"password doesnot match")
        else:
            myuser = User.objects.create_user(Username,Email,Pass1)
            myuser.save()
            messages.success(request, "sucesss")
            return HttpResponseRedirect('todo/')
        
          
    else:
        return HttpResponse("404 -page forbiden")


def handlelogout(request):
    logout(request)
    messages.success(request, "sucesssfully logged out")
    return redirect('home')
        

def handlelogin(request):
        if request.method == 'POST':
            LoginPass1 = request.POST['LoginPass1']
            LoginUsername = request.POST['LoginUsername']

        user = authenticate(username=LoginUsername,password=LoginPass1)

        if user is not None:
            login(request,user)
            messages.success(request, "sucesss")
            return HttpResponseRedirect('todo/')

        else:
            messages.error(request,"check your")
            return redirect('home')


# Create your views here.

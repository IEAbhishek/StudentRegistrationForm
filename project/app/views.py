from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import models
from .models import Contact

def index(request):
    return render(request,'index.html')

def handleSignup(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address1=request.POST.get('address1','')
        address2=request.POST.get('address2','')
        state=request.POST.get('state','')
        phoneno=request.POST.get('phoneno','')
        if name and email and address1 and address2 and state and phoneno:
            contact=Contact(name=name,email=email,address1=address1,address2=address2,state=state,phoneno=phoneno)
            contact.save()
        else:
            messages.error('Invalid Credentials')
        # myuser=User.objects.create_user(name,email)
        # myuser.email=email
        # myuser.address1=address1
        # myuser.address2=address2
        # myuser.state=state
        # myuser.phoneno=phoneno
        # myuser.save()
        messages.success(request,'Uploaded successful')
    return render(request,'index.html')
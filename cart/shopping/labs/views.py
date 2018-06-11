from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import labs,services
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method== 'POST':
        Username=request.POST.get('Username')
        Firstname=request.POST.get('Firstname')
        Lastname=request.POST.get('Lastname')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        
        user = User.objects.create_user(
            username=Username,
            first_name=Firstname,
            last_name=Lastname,
            email=Email,
            password=Password
        )
        
        return render(request,'labs/signin.html')
    return render(request,'labs/signup.html')



def signin(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
   
        if user is not None:
            login(request, user)
            request.session['name']=user.username
            
            
            return HttpResponseRedirect('/labsatcall/shop')
        else:
            x=" User Name or Password is incorrect !!"
            return render(request,'labs/signin.html',{'x':x})
        
    return render(request,'labs/signin.html')


def signout(request,):
    logout(request)
    return render(request,'labs/signout.html')

@login_required(login_url='/labsatcall/')
def addlabs(request):
    if request.method== 'POST':
        Name=request.POST.get('Name')
        Address=request.POST.get('Address')
        Email=request.POST.get('Email')
        Contactno=request.POST.get('Contactno')
        Description=request.POST.get('Description')
        
        obj = labs.objects.create(
            Name=Name,
            Address=Address,
            Email=Email,
            Contactno=Contactno,
            Description=Description
        )
        
        return render(request,'labs/addlabs.html')
    return render(request,'labs/addlabs.html')


@login_required(login_url='/labsatcall/')
def addservices(request):
    if request.method== 'POST':
        Labname=request.POST.get('Labname')
        Servicename=request.POST.getlist('Servicename')
        Servicecode=request.POST.getlist('Servicecode')
        Price=request.POST.getlist('Price')
        Description=request.POST.getlist('Description')
        n=len(Servicename)
        for i in range(n):
            obj=services.objects.create(
                Labname=Labname,
                Servicename=Servicename[i],
                Servicecode=Servicecode[i],
                Price=Price[i],
                Description=Description[i],            
            )
        
        return HttpResponseRedirect('/labsatcall/services')
    queryset=labs.objects.values('Name').distinct()
    return render(request,'labs/addservices.html',{'object':queryset})

@login_required(login_url='/labsatcall/')
def shop(request):
    queryset=services.objects.all()
    return render(request,'labs/services.html',{'object':queryset})
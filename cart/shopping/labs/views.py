from django.shortcuts import render
from django.http import HttpResponse
from . models import labs

# Create your views here.

def index(request):
    if request.method== 'POST':
        Name=request.POST.get('Name')
        Address=request.POST.get('Address')
        Email=request.POST.get('Email')
        Telno=request.POST.get('Telno')
        
        obj=labs.objects.create(
            Name=Name,
            Address=Address,
            Email=Email,
            Telno=Telno
        )
        
        return render(request,'labs/index.html')
    return render(request,'labs/index.html')
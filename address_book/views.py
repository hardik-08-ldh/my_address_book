from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'home.html',{})

def AddAddressView(request):
    return render(request,'add_address.html',{})
from django.shortcuts import render,redirect
from address_book import models,forms
from django.contrib import messages
# Create your views here.

def Home(request):
    all_addresses=models.Address.objects.all
    return render(request,'home.html',{'all_addresses':all_addresses})

def AddAddressView(request):
    if request.method=="POST":
        form=forms.AddAddressForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("Address has been added successfully!!😊😊"))
            return redirect('home')
        else:
            messages.success(request,("There was an error while submitting the form!!😢😢"))
            return render(request,'add_address.html',{})
    else:
        return render(request,'add_address.html',{})

def EditAddressView(request,list_id):
    if request.method=="POST":
        currrent_address=models.Address.objects.get(id=list_id)
        form=forms.AddAddressForm(request.POST or None,instance=currrent_address)
        if form.is_valid():
            form.save()
            messages.success(request,("Address has been edited successfully!!😊😊"))
            return redirect('home')
        else:
            messages.success(request,("There was an error while submitting the form!!😢😢"))
            return render(request,'edit.html',{})
    else:
        get_address=models.Address.objects.get(id=list_id)
        return render(request,'edit.html',{'get_address':get_address})

def DeleteView(request,list_id):
    if request.method=="POST":
        cur_address=models.Address.objects.get(id=list_id)
        cur_address.delete()
        messages.success(request,("Address has been deleted successfully!!! 😊😊"))
        return redirect('home')
    else:
        messages.warning(request,("You are not allowed here 😡😡"))
        return redirect('home')
from django.shortcuts import render,redirect
from .models import Inputab,current_position
import requests
# Create your views here.
def index(request):
    if request.method=='POST':
        location=request.POST.get('location','')
        pos=current_position(location=location)
        pos.save()
    inputs=Inputab.objects.all().order_by('-date_posted')
    #location1=current_position.objects.all().order_by('-date_posted')
    feed={'inputs':inputs}
    #combine=zip(inputs,location1)
    #feed2={'combine':combine}
    return render(request,'day_to_diary/index.html',feed)

def add(request):
    if request.method=='POST':
        first=request.POST.get('first','')
        last=request.POST.get('last','')
        report=request.POST.get('report','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        address2=request.POST.get('address2','')
        state=request.POST.get('state','')
        state_zip=request.POST.get('zip','')
        input=Inputab(first=first,last=last,report=report,phone=phone,email=email,address=address
                ,address2=address2,state=state,state_zip=state_zip)
        input.save()        
    return render(request,'day_to_diary/add.html')    

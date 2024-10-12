from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Dates
def home(request):
    msg = "<h1> Hello world </h1>"
    return HttpResponse(msg)
def index(request):
    return HttpResponse("<h1> It is the index</h1>")

from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

def h(request):
    # result = os.path.join(BASE_DIR,"template")
    # print(result)
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']
        
        obj=Dates()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Mail=mail
        obj.save()

    return render(request,'home.html')

def product(request):
    mobile = int(request.GET["mobile"])
    pc = int(request.GET["pc"])
    mouse = int(request.GET["mouse"])
    price = mobile+pc+mouse
    return render(request,'result.html',{"price":price})
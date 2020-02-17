from django.shortcuts import render,HttpResponse
import templates
from .form import *
# Create your views here.
def bulb(request):
    if request.method == "POST":
        form = bulbstatus_form(request.POST)
        f = form.save(commit=False)
        f.on = request.POST["value"]
        # f.off = request.POST['nothing']
        f.save()
        HttpResponse("hi saved remove me")
    return render(request, "index.html")
def home(request):
    return render(request,"home.html")

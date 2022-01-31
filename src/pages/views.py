from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwagrs):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"./pages/home.html",{})

def contact_view(request,*args,**kwagrs):
    return render(request,"./pages/contact.html",{})

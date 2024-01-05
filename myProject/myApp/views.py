from django.shortcuts import render

# Create your views here.

def hello(request):
    h = 1
    context = {}
    return render(request,"myApp/hello.html" ,context)

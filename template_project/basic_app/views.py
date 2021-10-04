from django.shortcuts import render

def index(request):
    index_dict = {"text":"HELLO WORLD" , "number" : 100}
    return render(request , "basic_app/index.html" , index_dict)

def other(request):
    return render(request , "basic_app/other.html")

def relative(request):
    return render(request , "basic_app/relative_url.html")

# Create your views here.

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def ajax1(request):
    return HttpResponse("ajax1")

def ajax2(request):
    return HttpResponse("ajax2")

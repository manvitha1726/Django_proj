from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def myths(request):
    return render(request,'myths.html')
def pros(request):
    return render(request,'pros.html')
def cons(request):
    return render(request,'cons.html')
def contact(request):
    return render(request,'contact.html')

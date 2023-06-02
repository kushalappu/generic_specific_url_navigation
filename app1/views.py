from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rahul(request):
    return HttpResponse('hiii i am rahul')

def rashid(request):
    return render(request,'gt.html')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return render(request,'rcb.html')

def fap(request):
    return HttpResponse('hiii i am fap')
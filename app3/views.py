from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('hii iam dhoni')

def sewag(request):
    return render(request,'india.html')

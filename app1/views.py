from django.shortcuts import render

# Create your views here.
def virat(request):
    return render(request,'rcb.html')

def rashid(request):
    return render(request,'gt.html')
from django.shortcuts import render

# Create your views here.
def mdb_jquery(request):
    return render(request,'mdb_jquery.html')

def web(request):
    return render(request,'web.html')
from django.shortcuts import render
from django.template import loader

def login(request):
	return render(request,'logn/login.html')
def index(request):
    return render(request, 'logn/intro.html')

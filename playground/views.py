from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    x = 1
    x = 2
    return render(request, 'hello.html', { 'name': 'Werner'})

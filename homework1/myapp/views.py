#userB


from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("test")

def bweb(request):
    print("hello")
    return HttpResponse("hello world")
#userA
from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("test")
def aweb(request):
    return HttpResponse("hello,world")
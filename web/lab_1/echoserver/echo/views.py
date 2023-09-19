from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView(req):
    return HttpResponse('Hello world from home page!')

def aboutPageView(req):
    return HttpResponse('Hello from another view that contains info about this app')

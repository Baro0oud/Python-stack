from django.shortcuts import render, HttpResponse , redirect 
from django.http import JsonResponse
def root(request):
    return redirect("/blogs")
# Create your views here.


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")


def show(request,number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request,number):
    return HttpResponse(f"placeholder to display blog number:{number}")

def destroy(request,number):
    return redirect("/blogs")

def json(request):
    data={
        'title':'my first blog',
        'content':'axsos'
    }
    return JsonResponse(data)
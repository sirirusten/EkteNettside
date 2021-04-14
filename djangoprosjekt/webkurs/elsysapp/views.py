from django.shortcuts import render
from django.middleware import csrf
from django.http import QueryDict
import requests
from django.http import HttpResponse, QueryDict, JsonResponse



def index(request):
    print("Dette blir printa i terminalen")
    context = {} # Tom dictionary som blir brukt senere!
    return render(request, "elsysapp/index.html", context)

def bane1(request):
    print("Jeg vil se Bane1.")
    f = open('elsysapp/static/Resultater.txt', 'r')
    file_content = f.read()
    f.close()

    content_list = file_content.split("\n")
    lagA = content_list[0].split(",")
    lagB = content_list[1].split(",")

    context = {'lagA' : lagA, 'lagB' : lagB}
    return render(request, "elsysapp/bane1.html", context)

def bane2(request):
    print("Jeg vil se Bane2.")
    context = {}
    return render(request, "elsysapp/bane2.html", context)

def bane3(request):
    print("Jeg vil se Bane3.")
    context = {}
    return render(request, "elsysapp/bane3.html", context)

def bane4(request):
    print("Jeg vil se Bane4.")
    context = {}
    return render(request, "elsysapp/bane4.html", context)

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! Wou're at the polls index.")

##simplest view possible in Django
##Now, to call this view, it needs to be mapped to a url(for an url we need a
## URLconf)

##Hence to create a URLconf in the polls directory, we create the file urls.py

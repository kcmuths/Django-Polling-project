##This file is created to map the views url here. More info in the comments
##of the view file

from django.conf.urls import url

from . import views ##importing views.py 

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

## urlpattern explanation:
##the 'r' in front of regular expression tells python the string is raw. Basical##ly meaning nothing in the string should be escaped
##Regular expressions: ^ means beginning of text, $ means end of text.
##The "name = index" is the name of the url used ot identify the view. Can give ##any name  

##SOME MORE NOTES: 
""" The function url() is passed 4 arguments. 2 required and 2 optional
Required arguments: url()argument:regex and url() argument:view. Django captures an HttpRequest object as the first argument 
Check out page: https://docs.djangoproject.com/en/1.9/intro/tutorial01/ for more details
"""

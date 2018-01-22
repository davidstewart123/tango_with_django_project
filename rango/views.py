# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #construct a dictionary to pass to the template engine as its context.
    #Note the key boldmessage is the same as {{ boldmessage }}in the template!
    context_dict = {'boldmessage': "Crunchy, creamie, cookie, candy, cupcake!"}

    #Return a rendered response to send to the client.
    #We make use of the shortcut function to make our lives easier.
    #Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    #htmla = "Rango says here is the about page" + '<a href="/rango/">Index</a>'
    return render(request, 'rango/about.html')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
    #Query the database for a list of ALL categories and pages currently stored.
    #Order the categories by no. likes and pages by no. views in descending order.
    #Retrieve the top 5 only - or all if less than 5.
    #Place the list in our context_dict dictionary
    #This will be passed to the template engine
    context_dict = {}

    category = Category.objects.order_by('-likes')[:5]

    pages = Page.objects.order_by('-views')[:5]

    context_dict['pages'] = pages

    context_dict['categories'] = category

    #Return the rendered response and sent it back!
    return render(request, 'rango/index.html', context_dict, context_dict)
def about(request):
    return render(request, 'rango/about.html')
def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)
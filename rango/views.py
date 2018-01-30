# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm

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
def add_category(request):
    form = CategoryForm()

    #A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        #have we been provided by a valid form?
        if form.is_valid():
            form.save(commit=True)
            #Now that the category is saved
            #we could give a confirmation message
            #But since the most recent category added is on the index page
            #THen we can direct the user back to the index page.
            return index(request)
        else:
            #The supplied form contained errors -
            #just print them in the terminal
            print(form.errors)
    #Will handle the bad form, new form, or no form supplied cases.
    #Render the form with error messages (if any)
    return render(request, 'rango/add_category.html', {'form': form})
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)



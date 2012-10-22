from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

def index(request):
    previous_button = {'text':'Yahoo', 'url':'http://www.yahoo.com'}
    next_button = {'text':'Google', 'url':'http://www.google.com'}

    context = {
        'page_title': 'Main page',
        'previous_button': previous_button,
        'next_button': next_button,
    }
    return render(request, 'macro/index.html', context)

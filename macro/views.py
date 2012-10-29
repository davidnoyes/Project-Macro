from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.utils import simplejson
import os

def index(request):

    context = {
        'top_bar_colour': 'transparent', #blue, black, transparent
        'page_title': 'Project: Macro',
        
        #'left_arrow_button': [{'text':'Yahoo', 'url':'http://www.yahoo.com', 'isHome':True},{'text':'Google', 'url':'http://www.google.com'}],
        #'right_arrow_button': [{'text':'Yahoo', 'url':'http://www.yahoo.com', 'isHome':True},{'text':'Google', 'url':'http://www.google.com'}],
        
        #'left_button':{'text':'Google', 'url':'http://www.google.com','blue':False},
        #'right_button': {'text':'Google', 'url':'http://www.google.com','blue':False},
        
        #'duo_selection_buttons': [{'text':'Yahoo', 'url':'http://www.yahoo.com', 'active': True},{'text':'Google', 'url':'http://www.google.com', 'active':False}],
        #'tri_selection_buttons': [{'text':'Yahoo', 'url':'http://www.yahoo.com', 'active': True},{'text':'Google', 'url':'http://www.google.com', 'active':False},{'text':'Bing', 'url':'http://www.bing.com', 'active':False}],
        
        #'duo_button': [{'text':'Yahoo', 'url':'http://www.yahoo.com', 'active': True},{'text':'Google', 'url':'http://www.google.com', 'active':False}],
        #'tri_button': [{'text':'Yahoo', 'url':'http://www.yahoo.com', 'active': True},{'text':'Google', 'url':'http://www.google.com', 'active':False}],
        
        'right_button': {'text':'Settings', 'url':'/macro/settings/'},
    }
    return render(request, 'macro/index.html', context)

def settings(request):
    context = {
        'top_bar_colour': 'transparent',
        'page_title': 'Settings',
        
        'left_arrow_button': [{'url':'/macro/', 'isHome':True},],
        'right_button': {'text': 'Power', 'url':'/macro/settings/power/'},
    }
    return render(request, 'macro/settings.html', context)

def power(request):
    context={
        'top_bar_colour': 'transparent',
        'page_title': 'Power',
        'left_arrow_button': [{'url':'/macro/', 'isHome':True},{'text':'Settings','url':'/macro/settings/'},],
    }
    if request.method == "POST":
        if (request.POST["command"] == "off"):
            os.system('sudo shutdown -h now') #Add -k to test and not actually shut down
            return HttpResponse(simplejson.dumps("Powering Off..."), mimetype='application/javascript')
            
    return render(request, 'macro/power.html', context)
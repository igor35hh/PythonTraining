# -*- coding: cp1251 -*-
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def welcome(request):
    return HttpResponse("Welcome")

def hello(request):
    return HttpResponse("Hello world")

def time(request):
    now = datetime.datetime.now()
    current_date = datetime.datetime.now()
    
    #html = "<html><body>Now is %s.</body></html>" % now
    #return HttpResponse(html)
    #t = Template("<html><body>Now is {{current_date}} </body></html>")
    
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    
    #return HttpResponse(html)
    return render_to_response('current_datetime.html', locals());
    #return render_to_response('current_datetime.html', {'current_date': now});

def timeplus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>After %s hours will %s</body></html>" % (offset, dt)
    return HttpResponse(html)

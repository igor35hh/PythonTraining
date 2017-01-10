# -*- coding: cp1251 -*-
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime
from books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from forms import ContactForm

def welcome(request):
    return HttpResponse("Welcome")

def hello(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html)) 
    #return HttpResponse("Hello world")

def search_form(request):
    errors = []
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search query.')
        elif len(q)> 20:
            errors.append('Enter a search query less then 20 letters.')
        else: 
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books':books, 'query':q})

    return render_to_response('search_form.html', {'errors': errors})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponseRedirect('/contact/thanks/') 
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get['email', 'noreply@example.com'],
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')    
    else:
        form = ContactForm(
            initial={'subject':'It is cool site!'}
        )
        return render_to_response('contact_form.html', {'form':form})
    
    #errors = []
    #if request.method == 'POST':
    #    if not request.POST.get('subject', ''):
    #        errors.append('Enter the theme.')
    #    if not request.POST.get('message', ''):
    #        errors.append('Enter the message.')
    #    if not request.POST.get('e-mail') and '@' not in request.POST['e-mail']:
    #        errors.append('Enter the right e-mail.')
    #    if not errors:
    #        #return HttpResponseRedirect('/contact/thanks/')
    #        send_mail(
    #            request.POST['subject'],
    #            request.POST['message'],
    #            request.POST.get['e-mail', 'noreply@example.com'],
    #            ['siteowner@example.com'],
    #        )
    #    return HttpResponseRedirect('/contact/thanks/')
    #return render_to_response('contact_form.html', {
    #    'errors': errors,
    #    'subject': request.POST.get('subject', ''),
    #    'message': request.POST.get('message', ''),
    #    'email': request.POST.get('e-mail', '')
    #})

def contact_thanks(request):
    return render_to_response('contact_thanks.html')

def time(request):
    now = datetime.datetime.now()
    current_date = datetime.datetime.now()
    
    #html = "<html><body>Now is %s.</body></html>" % now
    #return HttpResponse(html)
    #t = Template("<html><body>Now is {{current_date}} </body></html>")
    
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    
    #return HttpResponse(html)
    return render_to_response('current_datetime.html', locals())
    #return render_to_response('current_datetime.html', {'current_date': now})

def timeplus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>After %s hours will %s</body></html>" % (offset, dt)
    return HttpResponse(html)

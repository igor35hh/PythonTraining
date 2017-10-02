from django.shortcuts import render, redirect, render_to_response
from django.contrib.admin.views.decorators import staff_member_required

from django.http import HttpResponseRedirect
from .forms import UploadFileForm

from django.contrib import admin

from .admin import UserAdminNew

from django.contrib.auth.models import User
from django.contrib.admin.views.main import ChangeList 

def RenderToUser(request):
    
    template_name = 'admin/user_change_list.html' 
    
    #UserAdminNew.render_to_user(request)
    
    UserAdminNew.change_list_template = template_name
    cl = ChangeList(request, UserAdminNew.model, UserAdminNew.list_display, UserAdminNew.list_display_links, UserAdminNew.list_filter, 
                        UserAdminNew.date_hierarchy, UserAdminNew.search_fields, UserAdminNew.list_select_related, UserAdminNew.list_per_page, 
                        UserAdminNew.list_max_show_all, UserAdminNew.list_editable, UserAdminNew)
    
    context = {
            'opts': User._meta,
            'title': cl.title,
            #'is_popup': cl.is_popup,
            'cl': cl,
            #'has_add_permission': self.has_add_permission(self, request),
            #'root_path': self.admin_site.root_path,
            #'app_label': app_label,
        }
    
    return render(request, template_name, context)
    


@staff_member_required
def DownloadCSV(request):
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            #print(file.name)
            #print(file.content_type)
            #print(file.size)
            #print(file.read())
            
            fileup = request.FILES['filename']
            with open('file.name', 'wb+') as destination:
                for chunk in fileup.chunks():
                    destination.write(chunk)
            
            with open('file.name', 'r') as fp:
                for line in fp:
                   print(line)
            
            return HttpResponseRedirect('/admin/auth/user/')
        else:
            return render(request, 'admin/download.html', {'error': True})
            
    else:
        return render(request, 'admin/download.html', {'error': True})
        
    

@staff_member_required
def Download(request, cl):
    data = {
        #'opts': cl.opts,
        #'app_label': cl.opts.app_label,
        'cl': cl,
        'error': False,    
        'has_permission': True,
        'has_change_permission': True,
        'is_popup': False,
        'add': False,
        'site_header': admin.site.site_header,
        'original': 'Download csv',
        'media': '',
        'verbose_name_plural':'users',
        'changelist':'authhhh',
        
        }
    return render(request, 'admin/download.html', data)
    #return HttpResponseRedirect('/admin/auth/user/')




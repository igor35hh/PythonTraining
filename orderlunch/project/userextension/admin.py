from django.contrib import admin
from django.contrib.auth.models import User
from functools import update_wrapper
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.contrib import messages

def handle_uploaded_file(filename):
    import string
    from random import choice
    alphabet = string.ascii_letters + string.digits
    with open(filename, 'r') as fp:
        for line in fp:
            name, lastname, email = line.split(';')
            username = name +' '+ lastname   
            password = ''.join(choice(alphabet) for i in range(8))
            print(username, email, password)
            #newuser = User.objects.create_user(username, email, password)
            print(line)

class UserAdminNew(admin.ModelAdmin):
    
    list_filter = ['username', 'email', 'is_active']
    
    def auth_user_downloadcsv(self, request):
        template_name = 'admin/download.html'
        self.change_list_template = template_name 
        context = self.admin_site.each_context(request)
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
            
                #print(file.name)
                #print(file.content_type)
                #print(file.size)
                #print(file.read())
                #fileup = request.FILES['filename']
                
                fileup = form.cleaned_data['filename']
                
                print(fileup.name, fileup.size)
                
                
                with open(fileup.name, 'wb+') as destination:
                    for chunk in fileup.chunks():
                        destination.write(chunk)
                                
                messages.add_message(request, messages.INFO, 'File has been dowloaded')
                        
                handle_uploaded_file(fileup.name)
                
                return HttpResponseRedirect('/admin/auth/user/')
            else:
                context.update({
                    'errors': True,
                    'original':'Download CSV',
                    'has_add_permission': self.has_add_permission(request),
                    'has_change_permission': self.has_change_permission(request, None),
                    'has_delete_permission': self.has_delete_permission(request, None),
                    'title':'Select scv',
                    'form': form,
                })
                return admin.ModelAdmin.changelist_view(self, request, context)
            
        else:
            context.update({
                    'errors': True,
                    'original':'Download CSV',
                    'has_add_permission': self.has_add_permission(request),
                    'has_change_permission': self.has_change_permission(request, None),
                    'has_delete_permission': self.has_delete_permission(request, None),
                    'title':'Select scv',
                })
            return admin.ModelAdmin.changelist_view(self, request, context)

    
    def auth_user_download(self, request):
        template_name = 'admin/download.html'
        self.change_list_template = template_name
        context = self.admin_site.each_context(request)
        form = UploadFileForm()
        context.update({
            'original':'Download CSV',
            'has_add_permission': self.has_add_permission(request),
            'has_change_permission': self.has_change_permission(request, None),
            'has_delete_permission': self.has_delete_permission(request, None),
            'title':'Select scv',
            'form': form,
        })
        return admin.ModelAdmin.changelist_view(self, request, context)
    
    def changelist_view(self, request, extra_context=None):
        template_name = 'admin/user_change_list.html'
        self.change_list_template = template_name
        return admin.ModelAdmin.changelist_view(self, request, extra_context=extra_context) 
    
    def get_urls(self):
        from django.conf.urls import url
        
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            wrapper.model_admin = self
            return update_wrapper(wrapper, view)
        
        urls = super().get_urls()
        
        info = self.model._meta.app_label, self.model._meta.model_name
        
        my_urls = [
            url(r'^downloadcsv/', wrap(self.auth_user_downloadcsv), name='%s_%s_downloadcsv' % info),
            url(r'^download/', wrap(self.auth_user_download), name='%s_%s_download' % info),
        ]

        return my_urls + urls
        

admin.site.unregister(User)
admin.site.register(User, UserAdminNew)

from django.contrib import admin

# Register your models here.

from .models import Question, Choise

#class ChoiseInline(admin.StackedInline):
class ChoiseInline(admin.TabularInline):
    model = Choise
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Data information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiseInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choise)

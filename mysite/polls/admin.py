from django.contrib import admin

from .models import Choice, Question,Report_master


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class ReportAdmin(admin.ModelAdmin):
    list_display = ['Report_desc','Report_path','Last_modf']
    list_filter = ['Last_modf']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Report_master, ReportAdmin)

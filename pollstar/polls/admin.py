from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Pollstar Admin"
admin.site.site_title = "Pollstar admin area"
admin.site.index_title = "Welcome to Pollstar admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('none', {'fields': ['questionText']}),
    ('Date Information', {'fields': ['pubDate'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Question, QuestionAdmin)


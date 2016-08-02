from django.contrib import admin
from django import forms
from maid.models import *
from redactor.widgets import RedactorEditor
from django.contrib import admin

class MaidAdmin(admin.ModelAdmin):
	list_display = ("image", "name", "types", "nationality", "dob", "height", "weight", "religion", "mstatus", "age",)

class AboutusForm(forms.ModelForm):
    class Meta:
        model = Aboutus
        widgets = {
           'short_text': RedactorEditor(),
        }

class AboutusAdmin(admin.ModelAdmin):
    form = AboutusForm


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        widgets = {
           'short_text': RedactorEditor(),
        }

class ServicesAdmin(admin.ModelAdmin):
    form = ServicesForm

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        widgets = {
           'short_text': RedactorEditor(),
        }

class HomeAdmin(admin.ModelAdmin):
    form = HomeForm


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        widgets = {
           'short_text': RedactorEditor(),
        }

class FaqAdmin(admin.ModelAdmin):
    form = FaqForm


admin.site.register(Maid, MaidAdmin)
admin.site.register(Agency)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Logo)
admin.site.register(Home, HomeAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Banner_Image)
admin.site.register(ContactForm)

from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from . import forms
# Create your views here.
class HomePage(TemplateView):
    template_name='index.html'

class InsertSchoolResource(CreateView):
    form_class=forms.InsertSchoolResource
    success_url='/isr'
    template_name='srm/insert_school_resource_form.html'

class InsertResourceType(CreateView):
    form_class=forms.InsertResourceType
    success_url='/isrt'
    template_name='srm/insert_school_resource_type_form.html'
    
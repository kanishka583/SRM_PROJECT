from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from . import forms
# Create your views here.
class SchoolSignUp(CreateView):
    form_class=forms.schoolCreationForm
    success_url='/'
    template_name='users/signup.html'


from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView
from . import forms
from django.urls import reverse
from . import models
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

class emptySlots(ListView):
    model=models.SchoolResource
    context_object_name='resources'
    ordering=['id']
    template_name='srm/viewemptyslots.html'

def bookslot1(request,id):
    record=models.SchoolResource.objects.get(id=id)
    record.h9_10=request.user.school
    record.save()
    return redirect('/emptyslots/')

def bookslot2(request,id):
    record=models.SchoolResource.objects.get(id=id)
    record.h10_11=request.user.school
    record.save()
    return redirect('/emptyslots/')

def bookslot3(request,id):
    record=models.SchoolResource.objects.get(id=id)
    record.h11_12=request.user.school
    record.save()
    return redirect('/emptyslots/')

def bookslot4(request,id):
    record=models.SchoolResource.objects.get(id=id)
    record.h1_2=request.user.school
    record.save()
    return redirect('/emptyslots/')

def bookslot5(request,id):
    record=models.SchoolResource.objects.get(id=id)
    record.h2_3=request.user.school
    record.save()
    return redirect('/emptyslots/')

def clearAllSlots(request):
    records=models.SchoolResource.objects.all()
    for record in records:
        record.h10_11=None
        record.h11_12=None
        record.h1_2=None
        record.h2_3=None
        record.h9_10=None
        record.save()
    return redirect('/emptyslots/')


    
from django import forms
from . import models

class InsertSchoolResource(forms.ModelForm):
    class Meta:
        model=models.SchoolResource
        fields=('name','resourceType','school')

class InsertResourceType(forms.ModelForm):
    class Meta:
        model=models.ResourceType
        fields=('name',)


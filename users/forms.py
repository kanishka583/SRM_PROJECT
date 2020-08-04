from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class schoolCreationForm(UserCreationForm):
    
    class Meta:
        model=models.School
        fields=('first_name','last_name','email','username','password1','password2')
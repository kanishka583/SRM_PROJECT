from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class School(User):

    def __str__(self):
        return "@{}".format(self.username)






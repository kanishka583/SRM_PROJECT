from django.db import models
from users.models import School
# Create your models here.

class ResourceType(models.Model):
    name=models.CharField(max_length=20)
    availability=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SchoolResource(models.Model):
    resourceType=models.ForeignKey(ResourceType,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    school=models.ForeignKey(School,related_name='resources',on_delete=models.CASCADE)

    h9_10=models.ForeignKey(School,related_name="h9_10",on_delete=models.DO_NOTHING,null=True,blank=True)
    h10_11=models.ForeignKey(School,related_name="h10_11",on_delete=models.DO_NOTHING,null=True,blank=True)
    h11_12=models.ForeignKey(School,related_name="h11_12",on_delete=models.DO_NOTHING,null=True,blank=True)
    h1_2=models.ForeignKey(School,related_name="h1_2",on_delete=models.DO_NOTHING,null=True,blank=True)
    h2_3=models.ForeignKey(School,related_name="h2_3",on_delete=models.DO_NOTHING,null=True,blank=True)

    def __str__(self):
        return "{}".format(self.school+" "+self.name)


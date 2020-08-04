from django.urls import path
from django.conf.urls import url
from . import views
app_name='srm'

urlpatterns=[
    url(r'^$',views.HomePage.as_view(),name="homepage"),
    url(r'isr/$',views.InsertSchoolResource.as_view(),name='isr'),
    url(r'isrt/$',views.InsertResourceType.as_view(),name="isrt")
]
from django.urls import path
from django.conf.urls import url
from . import views
app_name='srm'

urlpatterns=[
    url(r'^$',views.HomePage.as_view(),name="homepage"),
    url(r'^isr/$',views.InsertSchoolResource.as_view(),name='isr'),
    url(r'^isrt/$',views.InsertResourceType.as_view(),name="isrt"),
    url(r'^emptyslots/$',views.emptySlots.as_view(),name="emptyslots"),
    path('bookslot1/<int:id>/$',views.bookslot1,name='bookslot1'),
    path('bookslot2/<int:id>/$',views.bookslot2,name='bookslot2'),
    path('bookslot3/<int:id>/$',views.bookslot3,name='bookslot3'),
    path('bookslot4/<int:id>/$',views.bookslot4,name='bookslot4'),
    path('bookslot5/<int:id>/$',views.bookslot5,name='bookslot5'),
    url(r'^clearallslots/$',views.clearAllSlots,name='clearallslots')
]
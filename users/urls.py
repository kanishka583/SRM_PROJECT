from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name='users'

urlpatterns=[
    url(r'login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    url(r'logout/',auth_views.LogoutView.as_view(),name='logout'),
    url(r'signup/',views.SchoolSignUp.as_view(),name='signup')
]
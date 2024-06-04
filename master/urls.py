from django.urls import path
from master.views import *
urlpatterns = [
    path('',master_home,name='master_home'),
    path('master_registration',master_registration,name='master_registration'),
    path('master_login',master_login,name='master_login'),
    path('master_dashboard',master_dashboard,name='master_dashboard'),
]
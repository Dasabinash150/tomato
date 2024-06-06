from django.urls import path
from master.views import *
urlpatterns = [
    path('',master_home,name='master_home'),
    path('master_registration',master_registration,name='master_registration'),
    path('master_login',master_login,name='master_login'),
    path('add_item',add_item,name='add_item'),
    path('show_all_item',show_all_item,name="show_all_item"),
    path('master_dashboard',master_dashboard,name='master_dashboard'),
    path('update/<pk>',update,name="update"),
    path('delete/<pk>',delete,name="delete")
]
from django.urls import path
from customer import views as cv
urlpatterns = [
    path('register',cv.customer_registration,name="customer_registration"),
    path('customer_login',cv.customer_login,name="customer_login"),
    path('user_logout',cv.user_logout,name="user_logout"),

]

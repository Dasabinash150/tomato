from django.urls import path
from customer import views as cv
urlpatterns = [
    path('register',cv.customer_registration,name="customer_registration")
]

from django.urls import path

from .views import *

urlpatterns = [
    path('client/registration/', ClientRegistrationView.as_view()),
    path('employee/registration/', EmployeeRegistrationView.as_view()),
]

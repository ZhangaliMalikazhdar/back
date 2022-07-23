from django.shortcuts import render
from dj_rest_auth.registration.views import RegisterView
from user_management.serializers import *


class ClientRegistrationView(RegisterView):
    serializer_class = ClientRegistrationSerializer


class EmployeeRegistrationView(RegisterView):
    serializer_class = EmployeeRegistrationSerializer

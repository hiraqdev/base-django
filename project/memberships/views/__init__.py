from django.contrib.auth import logout
from django.shortcuts import redirect

from memberships.views.registration import RegistrationView
from memberships.views.login import LoginView
from memberships.views.forget_pass import ForgetPassView
from memberships.views.reset_code import ResetCodeView
from memberships.views.activation import ActivationView

def logout_view(request):
    logout(request)
    return redirect('memberships:login')

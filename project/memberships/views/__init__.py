from django.contrib.auth import logout
from django.shortcuts import redirect

from memberships.views.registration import RegistrationView
from memberships.views.login import LoginView
from memberships.views.reset_code import ResetCodeView

def logout_view(request):
    logout(request)
    return redirect('memberships:login')

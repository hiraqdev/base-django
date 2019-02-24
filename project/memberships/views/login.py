# pylint: disable=unused-argument
from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login

from commons.exceptions import ServiceValidationError, ServiceCallerError, ServiceAuthError
from memberships.forms import LoginForm
from memberships.services import LoginService

class LoginView(TemplateResponseMixin, View):
    template_name = 'memberships/login.html'

    def get(self, request):
        context = {}
        return self.render_to_response(context)

    def post(self, request):
        form = LoginForm(request.POST)
        auth = LoginService(request.POST, form, request=request)

        try:
            user = auth.validate().call()
            login(request, user)

            return redirect('dashboard:index')
        except ServiceAuthError as auth_err:
            messages.warning(request, auth_err.message)
        except ServiceValidationError as validation_err:
            messages.warning(request, validation_err.message)
        except ServiceCallerError as caller_err:
            messages.error(request, caller_err.message)

        return redirect('memberships:login')

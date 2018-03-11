from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.contrib import messages
from django.shortcuts import redirect

from commons.exceptions import ServiceValidationError, ServiceCallerError
from memberships.forms import RegistrationForm
from memberships.services import RegistrationService

class RegistrationView(TemplateResponseMixin, View):
    template_name = 'memberships/registration.html'

    def get(self, request):
        context = {}
        return self.render_to_response(context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        service = RegistrationService(request.POST, form)

        try:
            member = service.validate().call()
            messages.success(request, 'Your data has been saved')
        except ServiceValidationError:
            messages.warning(request, 'Invalid input fields, please try again')
        except ServiceCallerError:
            messages.error(request, 'Something went wrong, please try again')

        return redirect('memberships:registration')

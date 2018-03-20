from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.contrib import messages
from django.shortcuts import redirect, reverse

from commons.exceptions import ServiceValidationError, ServiceCallerError

from memberships.forms import ResetPassForm
from memberships.services import ResetPassService

class ResetCodeView(TemplateResponseMixin, View):
    template_name = 'memberships/reset_pass.html'

    def get(self, request, email, code):
        context = {'email': email, 'code': code}
        return self.render_to_response(context)

    def post(self, request, email, code):
        resetForm = ResetPassForm(request.POST)
        service = ResetPassService(request.POST, resetForm)

        try:
            service.validate().call()
            messages.success(request, 'Your password has been updated')
        except ServiceValidationError:
            messages.warning(request, 'Invalid input fields, please try again')
        except ServiceCallerError as exc_caller:
            print(exc_caller)
            messages.error(request, 'Something went wrong, please try again')

        return redirect(reverse('memberships:reset_code', kwargs={'email': email, 'code': code}))

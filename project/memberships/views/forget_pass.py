from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.contrib import messages
from django.shortcuts import redirect

from commons.exceptions import ServiceValidationError, ServiceCallerError

from memberships.forms import ForgotPassForm
from memberships.services import ForgotPassService

class ForgetPassView(TemplateResponseMixin, View):
    template_name = 'memberships/forget_pass.html'

    def get(self, request):
        context = {}
        return self.render_to_response(context)

    def post(self, request):
        forgotForm = ForgotPassForm(request.POST)
        service = ForgotPassService(request.POST, forgotForm)

        try:
            service.validate().call()
            messages.success(request, 'Your reset code link has been sent to your email')
        except ServiceValidationError:
            messages.warning(request, 'Invalid input fields, please try again')
        except ServiceCallerError:
            messages.error(request, 'Something went wrong, please try again')

        return redirect('memberships:forget_pass')

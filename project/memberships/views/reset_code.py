from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.contrib import messages
from django.shortcuts import redirect

from commons.exceptions import ServiceValidationError, ServiceCallerError
from memberships.services import ForgotPassService

class ResetCodeView(TemplateResponseMixin, View):
    template_name = 'memberships/reset_code.html'

    def get(self, request, email, code):
        pass

    def post(self, request, email, code):
        pass

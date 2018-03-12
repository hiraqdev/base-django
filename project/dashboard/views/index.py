from django.views import View
from django.views.generic.base import TemplateResponseMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.conf import settings

class IndexView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'dashboard/index.html'

    def get(self, request):
        context = {}
        return self.render_to_response(context)


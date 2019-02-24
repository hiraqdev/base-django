# pylint: disable=unused-argument, redefined-builtin, no-self-use, invalid-name
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

from memberships.models import Member

class ActivationView(View):

    def get(self, request, id, code):
        try:
            user = User.objects.get(pk=id)
            member = Member.objects.get(user=user)
        except (User.DoesNotExist, Member.DoesNotExist):
            messages.warning(request, 'Unknown user')
        else:
            if member.activation_code == code:
                user.is_active = True
                user.save()
                messages.success(request, 'Your account has been activated')
            else:
                messages.warning(request, 'Invalid code')

        return redirect('memberships:login')

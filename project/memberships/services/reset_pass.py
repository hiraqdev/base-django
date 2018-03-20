from django.contrib.auth.models import User

from commons.services import BaseService
from commons.exceptions import ServiceValidationError, ServiceCallerError

from memberships.models import Member

class ResetPassService(BaseService):

    def __init__(self, payload, validator):
        self._payload = payload
        super().__init__(validator)

    def validate(self):

        if not self._validator.is_valid():
            raise ServiceValidationError('Invalid payload')

        return self

    def call(self):
        email = self._payload.get('email')
        code = self._payload.get('reset_code')
        new_pass = self._payload.get('new_password')

        try:
            user = User.objects.get(email=email)
            member = Member.objects.get(user=user, reset_code=code)
        except Member.DoesNotExist:
            raise ServiceCallerError('Invalid member or reset code')
        except User.DoesNotExist:
            raise ServiceCallerError('Unknown user')
        else:
            # update user's password
            user.set_password(new_pass)
            user.save()

            # disable member request code states
            member.request_to_reset_pass = False
            member.reset_code = None
            member.save()

        return True

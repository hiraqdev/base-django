import shortuuid

from django.contrib.auth.models import User
from django.core import mail
from django.conf import settings
from django.urls import reverse

from commons.services import BaseService
from commons.exceptions import ServiceValidationError, ServiceCallerError

from memberships.models import Member

class ForgotPassService(BaseService):

    def __init__(self, payload, validator):
        self._payload = payload
        super().__init__(validator)

    def validate(self):
        if not self._validator.is_valid():
            raise ServiceValidationError('Invalid payload')

        return self

    def call(self):
        email = self._payload.get('email')
        code = shortuuid.ShortUUID().random(length=30)

        try:
            user = User.objects.get(email=email)
            member = Member.objects.get(user=user)
            member.request_to_reset_pass = True
            member.reset_code = code
            member.save()

            # prepare email content and params
            reset_code_link = settings.BASE_URL + reverse('memberships:reset_code', kwargs={'email': email, 'code': code})
            mail_content = """
            <html>
                <body>
                You have requesting a reset code for your account, please follow
                this link below : <br />
                {link}
                </body>
            </html>
            """.format(link=reset_code_link)

            # sending an email for reset code link
            mail_conn = mail.get_connection(as_html=True)
            mail.send_mail(
                'Membership - Request Reset Code',
                mail_content,
                settings.MEMBERSHIP_FROM_MAIL_RESET_CODE,
                [user.email],
                connection=mail_conn
            )

        except Member.DoesNotExist:
            raise ServiceCallerError('Member not found')
        except User.DoesNotExist:
            raise ServiceCallerError('User not found')
        except Exception as exc:
            raise ServiceCallerError(str(exc))

        return True

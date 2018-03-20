import shortuuid
from django.contrib.auth.models import User
from django.core import mail
from django.conf import settings
from django.urls import reverse

from commons.services import BaseService
from commons.exceptions import ServiceValidationError, ServiceCallerError

from memberships.models import Member

class RegistrationService(BaseService):
    """ Registration Service
    Is a service used when there are new members try to register
    them self to system.

    Required fields:
    - username
    - email
    - password
    """

    def __init__(self, payload, validator):
        """ Constructor

        Args:
            payload: Should be a dictionary contains key and value
            validator: An interface that provide is_valid() method
        """
        self._payload = payload

        # instantiate parent constructor
        super().__init__(validator)

    def validate(self):
        """ Validate

        Returns:
            RegistrationService instance

        Raises:
            commons.exceptions.ServiceValidationError: when not passed validation rules
        """
        if not self._validator.is_valid():
            raise ServiceValidationError('Invalid registration payload')

        # make it chainable
        return self

    def call(self):
        """ Call to running service

        Returns:
            Member

        Raises:
            commons.exceptions.ServiceCallerError: when something error happened
        """
        try:
            # we need to create a User object before save it to Member
            user = User.objects.create_user(
                self._payload.get('username'),
                self._payload.get('email'),
                self._payload.get('password')
            )

            user.is_active = False
            user.save()

            act_code = shortuuid.ShortUUID().random(length=22)

            member = Member()
            member.user = user
            member.activation_code = act_code
            member.save()

            # prepare email content and params
            activation_link = settings.BASE_URL + reverse('memberships:activation', kwargs={'id': user.id, 'code': act_code})
            mail_content = """
            <html>
                <body>
                Please click this link below : <br />
                {link}
                </body>
            </html>
            """.format(link=activation_link)

            # sending an email for reset code link
            mail_conn = mail.get_connection(as_html=True)
            mail.send_mail(
                'Membership - Activation',
                mail_content,
                settings.MEMBERSHIP_FROM_MAIL_ACTIVATION,
                [user.email],
                connection=mail_conn
            )

            return member
        except Exception as exc:
            raise ServiceCallerError(str(exc))

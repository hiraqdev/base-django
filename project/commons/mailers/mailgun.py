import requests

from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings

from commons.exceptions import MailerConfigError

class EmailBackend(BaseEmailBackend):

    def __init__(self, **kwargs):
        self.as_html = kwargs.get('as_html', False)

    def send_messages(self, email_messages):
        """A method to send a list of emails

        Args:
            email_messages: A list of EmailMessage objects

        Returns:
            Number of successfully delivered messages

        Raises:
            commons.exceptions.MailerConfigError
        """
        if settings.MAILGUN_API_KEY is None:
            raise MailerConfigError('Need mailgun api key')

        if settings.MAILGUN_DOMAIN is None:
            raise MailerConfigError('Need mailgun domain name')

        base_endpoint = 'https://api.mailgun.net/v3/{}/messages'.format(settings.MAILGUN_DOMAIN)
        success_resp = []

        if len(email_messages) >= 1:
            for email in email_messages:
                payload = {
                    'from': email.from_email,
                    'to': email.to,
                    'subject': email.subject
                }

                if self.as_html:
                    payload.update({'html': email.body})
                else:
                    payload.update({'text': email.body})

                resp = requests.post(
                    base_endpoint,
                    auth=('api', settings.MAILGUN_API_KEY),
                    data=payload
                )

                if resp.status_code == 200:
                    success_resp.append(resp.json().get('id'))

        return len(success_resp)

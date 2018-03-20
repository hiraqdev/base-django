from faker import Faker
from django.test import TestCase
from django.core import mail
from django.contrib.auth.models import User

from commons.exceptions import ServiceValidationError, ServiceCallerError

from memberships.forms import RegistrationForm, ForgotPassForm
from memberships.services import RegistrationService
from memberships.services import ForgotPassService
from memberships.models import Member

class TestForgotPassService(TestCase):

    def _register_user(self):
        password = self.faker.word()
        email = self.faker.free_email()

        payload = {
            'username': self.faker.user_name(),
            'email': email,
            'password': password,
            'password_confirm': password
        }

        form = RegistrationForm(payload)
        registration = RegistrationService(payload, form)
        member = registration.validate().call()
        return member

    def setUp(self):
        self.faker = Faker()

    def test_forgot_pass_success(self):
        member = self._register_user()
        payload = {'email': member.user.email}

        form = ForgotPassForm(payload)
        forgot_pass_service = ForgotPassService(payload, form)
        forgot_pass = forgot_pass_service.validate().call()

        self.assertTrue(forgot_pass)
        self.assertEqual(len(mail.outbox), 1)
        self.assertTrue(member.user.email in mail.outbox[0].to)

        member = Member.objects.get(user=member.user)
        self.assertTrue(member.request_to_reset_pass)
        self.assertIsNotNone(member.reset_code)

    def test_invalid_validation(self):
        payload = {'email': 'testing'}
        form = ForgotPassForm(payload)
        forgot_pass_service = ForgotPassService(payload, form)

        with self.assertRaises(ServiceValidationError):
            forgot_pass_service.validate()

    def test_unknown_user(self):
        payload = {'email': 'testing@test.com'}
        form = ForgotPassForm(payload)
        forgot_pass_service = ForgotPassService(payload, form)

        with self.assertRaises(ServiceCallerError):
            forgot_pass_service.validate().call()

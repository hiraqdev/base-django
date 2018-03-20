import shortuuid

from faker import Faker
from django.test import TestCase
from django.core import mail
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from commons.exceptions import ServiceValidationError, ServiceCallerError

from memberships.forms import RegistrationForm, ForgotPassForm, ResetPassForm
from memberships.services import RegistrationService
from memberships.services import ForgotPassService, ResetPassService
from memberships.models import Member

class TestResetPassService(TestCase):

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

        user = User.objects.get(email=email)
        user.is_active = True
        user.save()
        return member

    def _user_forgot(self):
        member = self._register_user()
        payload = {'email': member.user.email}

        form = ForgotPassForm(payload)
        forgot_pass_service = ForgotPassService(payload, form)
        forgot_pass = forgot_pass_service.validate().call()

        member = Member.objects.get(user=member.user)
        return member

    def setUp(self):
        self.faker = Faker()

    def test_success_to_reset(self):
        member = self._user_forgot()
        password = shortuuid.uuid()

        payload = {
            'email': member.user.email,
            'new_password': password,
            'new_password_confirm': password,
            'reset_code': member.reset_code
        }

        form = ResetPassForm(payload)
        reset_pass_service = ResetPassService(payload, form)
        reset_pass = reset_pass_service.validate().call()
        self.assertTrue(reset_pass)

        user_authenticated = authenticate(email=member.user.email, password=password)
        self.assertIsNotNone(user_authenticated)

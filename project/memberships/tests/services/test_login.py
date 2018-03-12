from faker import Faker
from django.test import TestCase
from django.contrib.auth.models import User

from commons.exceptions import ServiceValidationError, ServiceAuthError

from memberships.forms import LoginForm, RegistrationForm
from memberships.services import LoginService, RegistrationService
from memberships.models import Member

class TestLoginService(TestCase):

    def setUp(self):
        self.faker = Faker()

    def test_login_success(self):
        password = self.faker.word()
        email = self.faker.free_email()

        payload = {
            'username': self.faker.user_name(),
            'email': email,
            'password': password,
            'password_confirm': password
        }

        form_reg = RegistrationForm(payload)
        registration = RegistrationService(payload, form_reg)
        member = registration.validate().call()

        payload_login = {
            'email': email,
            'password': password
        }

        form_login = LoginForm(payload_login)
        login = LoginService(payload_login, form_login)
        user = login.validate().call()

        self.assertEqual(email, user.email)

    def test_invalid_credentials(self):
        payload_login = {
            'email': self.faker.free_email(),
            'password': self.faker.word()
        }

        form_login = LoginForm(payload_login)
        login = LoginService(payload_login, form_login)

        with self.assertRaises(ServiceAuthError):
            user = login.validate().call()

    def test_invalid_payload_invalid_email(self):
        payload_login = {
            'email': 'test',
            'password': self.faker.word()
        }

        form_login = LoginForm(payload_login)
        login = LoginService(payload_login, form_login)

        with self.assertRaises(ServiceValidationError):
            user = login.validate().call()

    def test_invalid_payload_invalid_password(self):
        payload_login = {
            'email': self.faker.free_email(),
        }

        form_login = LoginForm(payload_login)
        login = LoginService(payload_login, form_login)

        with self.assertRaises(ServiceValidationError):
            user = login.validate().call()

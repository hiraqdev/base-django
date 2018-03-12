from faker import Faker
from django.test import TestCase
from django.contrib.auth.models import User

from commons.exceptions import ServiceValidationError
from memberships.forms import RegistrationForm
from memberships.services import RegistrationService
from memberships.models import Member

class TestRegistrationService(TestCase):

    def setUp(self):
        self.faker = Faker()

    def test_payload_invalid_email(self):
        payload = {
            'username': self.faker.user_name(),
            'email': 'test',
            'password': self.faker.word(),
            'password_confirm': self.faker.word()
        }

        form = RegistrationForm(payload)
        registration = RegistrationService(payload, form)

        with self.assertRaises(ServiceValidationError) as exc:
            registration.validate()

    def test_payload_not_match_password(self):
        payload = {
            'username': self.faker.user_name(),
            'email': self.faker.free_email(),
            'password': self.faker.word(),
            'password_confirm': self.faker.word()
        }

        form = RegistrationForm(payload)
        registration = RegistrationService(payload, form)

        with self.assertRaises(ServiceValidationError) as exc:
            registration.validate()

    def test_registration_success(self):
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

        self.assertEqual(member.user.email, email)
        self.assertFalse(member.user.is_active)
        self.assertIsNotNone(member.activation_code)

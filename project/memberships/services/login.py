from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from commons.services import BaseService
from commons.exceptions import ServiceValidationError, ServiceCallerError, ServiceAuthError

class LoginService(BaseService):
    """ Login Service
    Is a service used to authenticate member
    and logged in to system.

    Required fields:
    - email
    - password
    """

    def __init__(self, payload, validator, request=None):
        """ Constructor

        Args:
            payload: Should be a dictionary contains key and value
            validator: An interface that provide is_valid() method
        """
        self._request = request
        self._payload = payload

        # instantiate parent constructor
        super().__init__(validator)

    def validate(self):
        """ Validate

        Returns:
            LoginService instance

        Raises:
            commons.exceptions.ServiceValidationError: when not passed validation rules
        """
        if not self._validator.is_valid():
            raise ServiceValidationError('Invalid login payload')

        # make it chainable
        return self

    def call(self):
        """ Call to running service

        Returns:
            Member

        Raises:
            commons.exceptions.ServiceCallerError: when something error happened
            commons.exceptions.ServiceAuthError: when credential is invalid
        """
        try:

            # authenticate user based on email and password
            user = authenticate(
                self._request,
                email=self._payload.get('email'),
                password=self._payload.get('password')
            )

            if user is None:
                raise ServiceAuthError('Invalid credentials')

            return user
        except ServiceAuthError as auth_error:
            raise ServiceAuthError(auth_error.message)
        except Exception as exc:
            raise ServiceCallerError(exc.message)

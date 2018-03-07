from abc import ABC, abstractmethod

class BaseService(ABC):
    """
    I'm using ServiceObject pattern like in Rails.
    With this pattern, we can moving all activities
    in controller to their services.  So we can
    accept a service as controller extensions.

    A service should has a dependencies injections
    maybe like form validations, a repository or a model
    or any classes or functions, and we should test all
    activities with or without their mocks.

    A service should have only one main activity, like:
    - registering new member -> one service
    - creating a shopping cart -> one service
    - etc

    We can chaining abstract methods like this:

    serviceA.validate().call()

    Depends on your needs.

    By default there are only two abstract methods:
    1. validate - anything relate to data validations
    2. call - used to run this main service function.
    """

    def __init__(self, validator):
        self._validator = validator

    @abstractmethod
    def validate(self):
        """
        Returns:
            anything you needs

        Raises:
            commons.exceptions.ServiceValidationError
        """
        pass

    @abstractmethod
    def call(self):
        """
        Returns:
            anything you needs

        Raises:
            commons.exceptions.ServiceCallerError
        """
        pass

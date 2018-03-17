class BaseException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class ServiceValidationError(BaseException):
    pass

class ServiceCallerError(BaseException):
    pass

class ServiceAuthError(BaseException):
    pass

class MailerConfigError(BaseException):
    pass

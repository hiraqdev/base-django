from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class Memberships(object):

    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            pwd_valid = check_password(password, user.password)
            if not pwd_valid:
                return None

            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

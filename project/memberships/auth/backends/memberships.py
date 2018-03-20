from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

from memberships.models import Member

class Memberships(object):

    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            pwd_valid = check_password(password, user.password)
            if not pwd_valid:
                return None

            if not user.is_active:
                return None

            member = Member.objects.get(user=user)
            if member.request_to_reset_pass:
                return None

            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

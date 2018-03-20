from django.db import models
from django.contrib.auth.models import User

from commons.models import BaseModel

class Member(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activation_code = models.CharField(max_length=255, db_index=True)
    request_to_reset_pass = models.BooleanField(default=False, db_index=True)
    reset_code = models.CharField(max_length=255, db_index=True, null=True, blank=True)

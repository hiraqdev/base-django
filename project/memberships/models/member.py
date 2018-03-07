from django.db import models
from django.contrib.auth.models import User

from commons.models import BaseModel

class Member(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activation_code = models.CharField(max_length=255, db_index=True)

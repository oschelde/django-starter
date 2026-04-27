from django.utils.translation import gettext_lazy as _

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from core.models import BaseTimestampedModel


class User(AbstractUser, BaseTimestampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    phone = models.CharField(max_length=16, unique=True, blank=True, null=True)
    phone_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(
        _("email verified at"), blank=True, null=True
    )

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_email(self):
        return self.email

    def __str__(self):
        return self.email

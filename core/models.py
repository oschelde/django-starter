from django.utils.translation import gettext_lazy as _

from django.db import models
from django.urls import reverse


class BaseTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

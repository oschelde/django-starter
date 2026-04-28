from allauth.account.signals import email_confirmed
from django.dispatch import receiver    
from django.utils import timezone


@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    print("Email confirmed signal received for email:", email_address)
    user = email_address.user
    user.email_verified_at = timezone.now()
    user.save()


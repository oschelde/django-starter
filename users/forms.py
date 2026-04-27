from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email",)


class UserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "phone",
        )


class UserSignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"placeholder": "First Name"})
    )

    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"placeholder": "Last Name"})
    )

    phone = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Phone"}),
    )

    def signup(self, request, user):

        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.phone = self.cleaned_data["phone"]
        user.save()

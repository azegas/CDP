from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "date_of_birth")

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email", "date_of_birth")

    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), )

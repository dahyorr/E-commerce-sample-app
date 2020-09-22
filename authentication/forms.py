from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from . import models


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'email')

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = models.User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_first_name(self):
        first_name = str(self.cleaned_data.get('first_name'))
        first_name = first_name.capitalize()
        return first_name

    def clean_last_name(self):
        last_name = str(self.cleaned_data.get('last_name'))
        last_name = last_name.capitalize()
        return last_name

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = models.User
        fields = ('first_name', 'last_name', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'email')


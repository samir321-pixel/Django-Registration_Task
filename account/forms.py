from django.core.exceptions import ValidationError
from django.forms import Form, CharField, EmailField, PasswordInput
from .models import *
from django import forms


class RegisterForm(Form):
    username = CharField()
    first_name = CharField()
    last_name = CharField()
    email = EmailField()
    password = CharField(widget=PasswordInput)
    password_confirm = CharField(widget=PasswordInput)

    def clean_password_confirm(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password_confirm'):
            raise ValidationError('Password fields do not match.')


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = '__all__'
        exclude = ['user']

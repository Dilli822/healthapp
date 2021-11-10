
from django import forms
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=128, widget=PasswordInput)


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    middle_name =forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    


    def clean_username(self):
        if User.objects.filter(username=self.cleaned_data['username']).exists():
            raise forms.ValidationError("This username is taken!Try another one.")
        return self.cleaned_data['username']
    
    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Your Passwords Donot Match!")





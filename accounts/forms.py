from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60,  widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email',
        }
    ))
    username = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter username',
        }
    ))
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Name',
        }
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password ',
        }
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Re-enter your Password',
        }
    ))

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1',
                  'password2', 'name')


class AuthenticationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your password',
    }))
    email = forms.EmailField(max_length=60, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email  address',
    }))

    class Meta:
        model = Account
        fields = (
            'email',
            'password',
        )

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Invalid Credentials")

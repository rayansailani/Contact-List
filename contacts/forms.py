from django import forms
from .models import Contact


class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'contact_number', 'description']

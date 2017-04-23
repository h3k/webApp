from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(min_length=30, required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email
from django import forms

class ForgotPassForm(forms.Form):
    email = forms.EmailField()

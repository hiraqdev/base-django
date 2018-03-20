from django import forms

class ResetPassForm(forms.Form):
    email = forms.EmailField()
    new_password = forms.CharField()
    new_password_confirm = forms.CharField()

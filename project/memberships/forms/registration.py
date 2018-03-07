from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    password_confirm = forms.CharField()

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('password_confirm')

        if password != confirm:
            raise forms.ValidationError('Given password not match')

        return confirm

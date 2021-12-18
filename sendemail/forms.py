from django import forms
from sendemail.models import Sendemail

# Forms do Revisão Manual
class SendEmailForm(forms.ModelForm):
    class Meta:
        model = Sendemail
        fields = '__all__' 
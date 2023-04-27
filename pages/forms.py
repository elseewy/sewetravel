from django import forms
from . models import Subscribers, MailMessage


class SubscibersForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "name": "email",
        "id": "email",
        "placeholder": "Enter your email address",
        "aria-label":"email address",
        "aria-describedby": "button-addon2",
    }), label="" )
    class Meta:
        model = Subscribers
        fields = ['email', ]


class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'

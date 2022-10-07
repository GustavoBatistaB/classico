from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    nome = forms.CharField(
        error_messages={'required': 'Este campo é obrigatório '},
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite o seu nome",
            }
        )
    )
    email = forms.CharField(
        error_messages={'invalid': 'Digite um e-mail válido!'},
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite o seu email"
            }
        )
    )
    mensagem = forms.CharField(
        error_messages={'required': 'O campo de mensagem é obrigatório'},
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua mensagem"
            }
        )
    )

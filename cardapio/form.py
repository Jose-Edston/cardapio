from django import forms
from cardapio import models


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ("__all__")

class CardapioForm(forms.ModelForm):
    class Meta:
        model = models.CardapioCliente
        fields = ("__all__")
from django import forms
from .models import Produto


class ProdutoForm(forms.Models):
    class Meta:
        model = Produto
        fields = '__all__'
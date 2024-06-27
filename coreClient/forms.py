from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = ['nome', 'email', 'servico', 'data_servico']
    widgets = {
      'nome': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'servico': forms.Select(attrs={'class': 'form-select'}),
      'data_servico': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    }
from django import forms
from core.models import RegistroModel
from django.forms import ModelForm

class RegistroForm(forms.Form):
    nome = forms.CharField(max_length=100)
    OPCOES_PROFESSOR = (
        ('Orlando Saraiva Jr', 'Orlando Saraiva Jr'),
        ('Thiago Mendes', 'Thiago Mendes'),
        ('Nilton', 'Nilton'),
        ('Sandro', 'Sandro'),
        ('Esdras', 'Esdras'),
        ('Ana Celia', 'Ana Celia'),
    )
    professor = forms.ChoiceField(choices=OPCOES_PROFESSOR)

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()
    
class RegistroModelForm(ModelForm):
    class Meta:
        model = RegistroModel
        fields = ['nome', 'professor']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()
    
from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['telefone'].widget.attrs.update({'class': 'mask-telefone'})
        self.fields['valor'].widget.attrs.update({'class': 'mask-valor'})
        self.fields['juros'].widget.attrs.update({'class': 'mask-juros'})
        self.fields['juros_mes'].widget.attrs.update(
            {'class': 'mask-pagamento'})
        self.fields['data_emprestimo'].widget.attrs.update(
            {'class': 'mask-data-emprestimo'})
        self.fields['vencimento_mensal'].widget.attrs.update(
            {'class': 'mask-vencimento'})
        self.fields['usuario'].widget = forms.HiddenInput()

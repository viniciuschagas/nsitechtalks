from django import forms

class FormularioDeContato(forms.Form):
    nome = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(max_length=200,required=True)
    assunto = forms.CharField(max_length=100,required=True)
    mensagem = forms.CharField(max_length=10000,required=True,widget=forms.Textarea())
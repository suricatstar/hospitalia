from django import forms

class formularioCadastro(forms.Form):
    nome = forms.CharField(max_length=30,label="Nome",widget=forms.TextInput(attrs={'class': 'form-control m-3'}))
    
    cpf = forms.CharField(max_length=11,label="Cpf", required=True,widget=forms.NumberInput(attrs={'class': 'form-control m-3'}))
    
    idade = forms.IntegerField(min_value=1, max_value=120,label="Idade", required=False,widget=forms.NumberInput(attrs={'class': 'form-control m-3'}))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control m-3'}))
    
    senha = forms.CharField(label="senha",widget=forms.TextInput(attrs={'class': 'form-control m-3'}))
    
    numero = forms.IntegerField(label="Número", required=False,widget=forms.NumberInput(attrs={'class': 'form-control m-3'}))
    
    
class formularioLogin(forms.Form):
    
    nome = forms.CharField(max_length=30,required=True,label="Nome",widget=forms.TextInput(attrs={'class': 'form-control m-3'}))
    
    senha = forms.CharField(label="senha",required=True,widget=forms.TextInput(attrs={'class': 'form-control m-3'}))
    
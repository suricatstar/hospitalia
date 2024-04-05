from django.shortcuts import render,redirect
from .models import Cliente
from django.http import HttpResponse

# Create your views here.
def cadastrarCliente(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nomeC = request.POST.get('nome')
        cpfC = request.POST.get('cpf')
        idadeC = request.POST.get('idade')
        emailC = request.POST.get('email')
        numC = request.POST.get('numero')
        
        cliente = Cliente(
            nome=nomeC,
            cpf=cpfC,
            idade=idadeC,
            email=emailC,
            numero=numC
        )
        
        cliente.save()
        return HttpResponse(f'{nomeC} - {cpfC} - {idadeC} - {emailC} - {numC}')

def loginCliente(request):
    return render(request, 'login.html')
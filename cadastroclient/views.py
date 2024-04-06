from django.shortcuts import render,redirect
from .models import Cliente
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def cadastrarCliente(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nomeC = request.POST.get('nome')
        cpfC = request.POST.get('cpf')
        idadeC = request.POST.get('idade')
        emailC = request.POST.get('email')
        senhaC = request.POST.get('senha')
        numC = request.POST.get('numero')
        
        cliente = Cliente(
            nome=nomeC,
            cpf=cpfC,
            idade=idadeC,
            email=emailC,
            numero=numC,
            senha=senhaC
        )
        
        cliente.save()
        return redirect(reverse('login_cliente'))

def loginCliente(request):
    emailL = request.GET.get('email')
    senhaL = request.GET.get('senha')
    correct = True
    
    print(request)
    print(emailL,senhaL)
    
    if emailL and senhaL:
    
        cliente = Cliente.objects.all()
        try:
            if cliente.filter(email=emailL).exists() and cliente.filter(senha=senhaL).exists():
                return HttpResponse(f'{emailL}-{senhaL}')
            
            else:    
                correct = False
                return render(request, 'login.html',{'correct': correct})
        except:
            return HttpResponse('estamos com problema no servidor')
    else:        
        return render(request, 'login.html')
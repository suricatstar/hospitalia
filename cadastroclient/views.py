from django.shortcuts import render,redirect
from .models import Cliente
from django.http import HttpResponse
from django.contrib.auth.models import User #importa o model user
from django.contrib.auth import authenticate,login #importa a funcao autenticate e o login

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
        
        user = User.objects.filter(email=emailC).first() 
        
        if not user:
            user = User.objects.create_user(username=nomeC, email=emailC,password=senhaC)
            
            cliente = Cliente(
                nome=nomeC,
                cpf=cpfC,
                idade=idadeC,
                email=emailC,
                numero=numC,
                senha=senhaC
            )
            user.save()
            cliente.save()
            return redirect(reverse('login_cliente'))
        else:
            confir= 'já existe usuário com esse email, tente logar'
            return render(request, 'login.html', {'confir': confir})

def loginCliente(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        nomeL = request.POST.get('nome')
        senhaL = request.POST.get('senha')
        correct = True
        
        if nomeL and senhaL:
            user = authenticate(username=nomeL, password=senhaL)
            try:
                if user:
                    login(request, user)
                    return redirect(reverse('consultas'))
                
                else:    
                    correct = False
                    return render(request, 'login.html',{'correct': correct})
            except:
                return HttpResponse('estamos com problema no servidor')
        else:        
            return render(request, 'login.html')
        
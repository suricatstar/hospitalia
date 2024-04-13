from django.shortcuts import render,redirect
from .models import Cliente
from django.http import HttpResponse
from django.contrib.auth.models import User #importa o model user
from django.contrib.auth import authenticate,login #importa a funcao autenticate e o login

from django.urls import reverse
from .forms import formularioCadastro,formularioLogin

# Create your views here.
def cadastrarCliente(request):
    if request.method == "GET":
        form = formularioCadastro()
        return render(request, 'cadastro.html', {'form': form})
    elif request.method == "POST":
        form = formularioCadastro(request.POST)
        if form.is_valid():
            nomeC = form.cleaned_data['nome']
            cpfC = form.cleaned_data['cpf']
            idadeC = form.cleaned_data['idade']
            emailC = form.cleaned_data['email']
            senhaC = form.cleaned_data['senha']
            numC = form.cleaned_data['numero']
            
            
            user = User.objects.filter(email=emailC).first() 
            
            #talvez dê para usar o forms.model
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
        else:
            return render(request, 'cadastro.html', {'form': form})

def loginCliente(request):
    if request.method == "GET":
        form = formularioLogin()
        return render(request,'login.html', {'form': form})
    else:
        form = formularioLogin(request.POST)
        if form.is_valid():
            nomeL = form.cleaned_data['nome']
            senhaL = form.cleaned_data['senha']
            correct = True
            
            if nomeL and senhaL:
                user = authenticate(username=nomeL, password=senhaL)
                try:
                    if user:
                        login(request, user)
                        return redirect(reverse('consultas'))
                    
                    else:    
                        correct = False
                        return render(request, 'login.html',{'correct': correct,'form': form})
                except:
                    return HttpResponse('estamos com problema no servidor')
            else:        
                return render(request, 'login.html', {'form': form})
        
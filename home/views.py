from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def plataforma(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponse('plataforma')
        return HttpResponse('você precisa estar logado')
        # return render(request, 'home.html')
    else:
        return HttpResponse('bosta')
        
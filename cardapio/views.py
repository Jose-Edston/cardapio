from django.shortcuts import render

from cardapio.form import UsuarioForm
from cardapio.models import CardapioCliente, Usuario


def index_cadastro(request):
    cadastro = Usuario.objects.all()
    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = UsuarioForm()
    return render(request, 'cardapio/pages/home.html', {"cadastro": cadastro, "form": form})


def index_login(request):
    return render(request, 'cardapio/pages/home.html')

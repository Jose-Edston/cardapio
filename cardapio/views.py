from django.shortcuts import render
from cardapio.models import CardapioCliente
from cardapio.models import Usuario
from cardapio.form import UsuarioForm

def index_cadastro(request):
    cadastro = Usuario.objects.all()
    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = UsuarioForm()
    return render(request, 'cadastro.html', {"cadastro": cadastro, "form":form})

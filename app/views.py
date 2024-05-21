from django.shortcuts import render, redirect
from app.forms import cadastroUsuarioForm, loginForm, transacaoForm, projetoForm, processoForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = projetoForm()
    return render(request, 'form.html', data)


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Cadastra um usuario novo"""
    if request.method != 'POST':
        #Exibe o formulario em branco de cadastro
        form = UserCreationForm()
    else:
        #Processa o formulario preenchido
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Faz o login do usuario e o redireciona para a pagina inicial
            login(request, new_user)
            return redirect('learning_logs:index')
        
    #Exibe um formulario em branco ou invalido
    context = {'form': form}
    return render(request, 'registration/register.html', context)
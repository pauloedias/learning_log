from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def check_topic_owner(request, topic):
    """
    Verifica se o usuário atual é o proprietário do tópico.
    Levanta Http404 se não for o caso.
    """
    if topic.owner != request.user:
        raise Http404("Você não tem permissão para acessar este tópico.")

def index(request):
    """A pagina inicial para o Registro de Aprendizagem"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Mostra todos os topicos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Mostra um unico topico e todas as suas entradas"""
    topic = Topic.objects.get(id=topic_id)
    #Verifica se o tópico pertence ao usuário atual
    check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Adiciona um topico novo"""
    if request.method != 'POST':
        #Nenhum dado enviado; cria um formulario em branco
        form = TopicForm
    else:
        #Dados POST enviados; processa os dados
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            form.save()
            return redirect('learning_logs:topics')
    #Exibe um formulario em branco ou invalido
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Adiciona uma entrada nova para um topico especifico"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #Nenhum dado enviado, cria um formulario em brnaco
        form = EntryForm()
    else:
        #Dados POST enviados; processa os dados
        form = EntryForm(data=request.POST)
        if topic.owner == request.user and form.is_valid:
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        else:
            raise Http404("Você não tem permissão para adicionar " +    
                          "novas entradas a esse tópico.")
    
    #Exibe um fomulário em branco ou inválido
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edita uma entrada existente"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)
    if request.method != 'POST':
        #Requisicão inicial: pré-preenche formulário com a entrada atual
        form = EntryForm(instance=entry)
    else:
        #Dados POST enviados; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

"""Define padrões de URL para learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Pagina inicial
    path('', views.index, name='index'),
    #Pagina que mostra todos os topicos
    path('topics/', views.topics, name='topics'),
    #Página de detalhes para um único tópico
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Pagina para adicionar um topico novo
    path('new_topic/', views.new_topic, name='new_topic'),
    #Pagina para adicionar uma nova entrada
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Pagina para editar um entrada
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
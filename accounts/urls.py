"""Define o padrao de urls para accounts"""

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    #inclui URLs de autenticacao default
    path('', include('django.contrib.auth.urls')),
    #Pagina de cadastro
    path('register/', views.register, name='register'),
]
from django.urls import path
from .import views as vs

app_name = 'core'

urlpatterns = [
    path('', vs.registrar, name='registrar'),
    path('listar', vs.listar, name='listar'),
]
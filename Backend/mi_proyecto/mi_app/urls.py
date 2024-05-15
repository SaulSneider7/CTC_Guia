from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_persona, name='registrar_persona'),
    path('lista/', views.lista_personas, name='lista_personas'),
]

from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import Persona

def registrar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'mi_app/registrar_persona.html', {'form': form})

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'mi_app/lista_personas.html', {'personas': personas})

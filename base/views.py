from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView  , DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tarea

# Create your views here.

class Logueo(LoginView):
    template_name="base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self) :
        return reverse_lazy('tareas')
    
class PaginaRegistro(FormView):
    template_name='base/registro.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url= reverse_lazy('tareas')
    
    def form_valid(self, form):
        usuario= form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)
    

class ListaPendientes(LoginRequiredMixin,ListView):
    model=Tarea
    context_object_name='tareas'
    
   

class DetalleTarea(LoginRequiredMixin,DetailView):
    model=Tarea
    context_object_name='tarea'
    template_name='base/tarea.html'

class CrearTarea(LoginRequiredMixin,CreateView): # crea un formulario de el modelo creado
    model=Tarea
    fields = '__all__'
    success_url= reverse_lazy('tareas')

class EditarTarea(LoginRequiredMixin,UpdateView):
    model=Tarea
    fields = '__all__'
    success_url= reverse_lazy('tareas')

class EliminarTarea(LoginRequiredMixin,DeleteView):
    model=Tarea
    context_object_name='tarea'
    success_url= reverse_lazy('tareas')
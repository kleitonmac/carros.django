from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#como por exemplo essa e uma funcao based view pois esta recebendo valor pelo view da pasta mae app


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
     
     
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
           cars = cars.filter(model__icontains=search)
        return cars
         
'''
List view tem um metodo de queryset que receber os filtros do campo de busca       
views orientadas a classes
função based view  ela utilza a Class import View e receber toda sua herança
    
    Create view viu de criacao de cadastro
'''

"""
  @method_decorator(login_required(login_url='login'), name='dispatch')
  metodo para passar uma camada de autentificacao vai mandar o cliente direto para fazer login 
"""
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'
    
    
    
class CarDetailView(DetailView):
        model = Car
        template_name = 'car_detail.html'
        
       
@method_decorator(login_required(login_url='login'), name='dispatch')        
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'      
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
      
      



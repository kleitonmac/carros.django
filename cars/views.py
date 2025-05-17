from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm


def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    
    if  search:   
        cars = cars.filter(model__icontains=search)
   
    
    return render(
        request, 
        'cars.html',
        {'cars': cars})

def new_car_view(request):
    #requisição de validação para o banco de dados method post e files para carregar arquivos
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():# ser meu if for valido cairá nesse campo
            new_car_form.save()
            return redirect('cars_list') # vai ser salvo no meu banco de dados e redirecionado
    else:
     new_car_form = CarModelForm()
    return render(request, 'new_car.html', { 'new_car_form': new_car_form })



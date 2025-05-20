from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View

#como por exemplo essa e uma funcao based view pois esta recebendo valor pelo view da pasta mae app
class CarsView(View):
    
    def get(self, request):
         cars = Car.objects.all().order_by('model')
         search = request.GET.get('search')
    
         if  search:   
             cars = cars.filter(model__icontains=search)
    
         return render(
        request, 
        'cars.html',
        {'cars': cars}
        )
#views orientadas a classes
#função based view  ela utilza a Class import View e receber toda sua herança
class NewCarView(View):
    
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', { 'new_car_form': new_car_form })
    
    def post(self , request):
        new_car_form = CarModelForm(request.POST , request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
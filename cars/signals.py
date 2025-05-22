from django.db.models.signals import  post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum




'''
Criação de signals 
'''
def car_inventory_update(): # criacao da função para registro de inventario
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value =Sum('value')
    )['total_value'] 
    CarInventory.objects.create(
        cars_count= cars_count,
        cars_value =cars_value
    ) #criaçao do registro no banco de dados

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
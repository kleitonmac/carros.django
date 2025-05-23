from django.db.models.signals import  post_save, post_delete,pre_save
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from openai_api.client import get_car_ai_bio


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

#signal da pre save da bio
@receiver(pre_save, sender=Car)
def car_pre_save(sender,instance , **kwargs):
       if not instance.bio:
           instance.bio="Bio gerada Automaticamente"
'''

   if not instance.bio:
    ai_bio = get_car_ai_bio(
        instance.model, instance.brand, instance.model_yaer
    )
    instance.bio = ai_bio
    
    Substituar a linha de codigo acima por essa e importe a biblioteca
    from openai_api.client import get_car_ai_bio
'''
    
   
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
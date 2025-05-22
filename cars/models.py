from django.db import models


class Brand(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=200)
        
        def __str__(self):
         return self.name
    
# tabela criada para meu banco de dados com chave primaria em brand(marca)
class Car(models.Model):
    id = models.AutoField(primary_key=True) 
    model =models.CharField(max_length=200) # modelo
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')    #marca
    factory_year = models.IntegerField() #ano de fabricação do carro
    model_year = models.IntegerField(blank=True , null=True) # ano de modelo do carro
    plate = models.IntegerField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True) # valor
    photo= models.ImageField(upload_to='cars_photos/', blank=True, null=True)# imagens que vai subir pro banco de dados e baixei o pip install pillow
    bio = models.TextField(blank=True, null=True, )
    
    
    def __str__(self):
        return self.model
    

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    #trecho de ordernacao pela class meta
    class Meta:
        ordering = ['-created_at']    
     
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'    
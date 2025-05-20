from django import forms
from cars.models import Brand, Car
from django.core.exceptions import ValidationError


class Carform(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()
     
    '''
    formulario 
    utlizado para salva no banco de dados avançado ele ja criar 
    um save so preciso comunicar com meu arquivo view passsando o parametro .save
    
    '''
class CarModelForm(forms.ModelForm):
    class Meta:
            model = Car
            fields = '__all__'
     
     #campos de validaçoes do  formulario dispará o erros de valores e exerção para permiter a validacao
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None and value < 10000:
            raise ValidationError('Valor mínimo do carro deve ser de R$ 10.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2000:
            self.add_error('factory_year', 'O ano dever ser maior que 2000')
        return factory_year
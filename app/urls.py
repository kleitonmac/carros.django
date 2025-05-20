# urls.py do projeto
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import  CarsView, NewCarView
from accounts.views import register_view, login_view, logout_view


#function based view uma url manda pra uma função
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('cars/',  CarsView.as_view(), name='cars_list'),
    path('new_car', NewCarView.as_view() , name='new_car'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

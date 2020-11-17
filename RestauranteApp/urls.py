from django.urls import path
from django.conf.urls.static import static 

from RestauranteApp import views


urlpatterns = [
    #Aqui van las views de la pagina web
    path('', views.home, name='home'),
    
]
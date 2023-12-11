from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('cabañas/<str:cabaña_id>', views.DetalleCabañas, name='cabañas'),
] 
    
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('cabañas/<str:cabaña_id>', views.DetalleCabañas, name='cabañas'),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='index.html'),name='logout'),
    path('cabañas/reserva/<int:cabaña_id>/',views.reserva,name='reserva'),
    path('reservas/cliente/<int:cliente_id>/', views.reservas_por_cliente, name='reservas_por_cliente'),
    path('pagar/<int:reservas_id>/',views.pagar,name='pagar'),
    path('gracias',views.gracias,name='gracias')
]

    
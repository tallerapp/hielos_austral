from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('cabañas/<str:cabaña_id>', views.DetalleCabañas, name='cabañas'),
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('cabañas/reserva/<int:cabaña_id>/',views.reserva,name='reserva')
] 
    
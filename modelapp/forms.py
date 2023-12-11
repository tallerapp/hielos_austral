from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Reserva,Cabaña
from django.contrib.auth.models import User

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['cabaña', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean(self):
        cleaned_data = super(ReservaForm, self).clean()
        cabaña = cleaned_data.get('cabaña')
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        # Asegúrate de que la fecha de inicio es anterior a la fecha de fin
        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            raise forms.ValidationError({
                'fecha_inicio': "La fecha de inicio debe ser antes de la fecha de fin.",
                'fecha_fin': "La fecha de fin debe ser después de la fecha de inicio."
            })
        
        # Comprueba la disponibilidad de la cabaña
        if fecha_inicio and fecha_fin:
            reservas_existentes = Reserva.objects.filter(
                cabaña=cabaña,
                fecha_fin__gte=fecha_inicio,
                fecha_inicio__lte=fecha_fin
            )
            if reservas_existentes.exists():
                raise forms.ValidationError("La cabaña no está disponible en las fechas seleccionadas.")
        
        return cleaned_data

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    username = forms.CharField(label='Nombre de usuario')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

from django.shortcuts import get_object_or_404, redirect, render
from modelapp.models import Cabaña
from .models import Reserva, User 

from .forms import ReservaForm, UserRegisterForm
from django.contrib.auth.decorators import login_required



def index(request):
    cabañas = Cabaña.objects.all();
    dict = { "datos": cabañas}
    
    return render(request,'index.html',dict)


def DetalleCabañas(request, cabaña_id):
    cabaña = get_object_or_404(Cabaña, cabaña_id=cabaña_id)
    return render(request, 'cabañas.html', {'cabaña': cabaña})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username'] 
            return redirect('web:login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request,'register.html',context)

@login_required
def reserva(request, cabaña_id):
    cabaña = get_object_or_404(Cabaña, pk=cabaña_id)

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            nueva_reserva = form.save(commit=False)
            nueva_reserva.cliente = request.user
            nueva_reserva.cabaña = cabaña
            nueva_reserva.save()

            return redirect('web:reservas_por_cliente', cliente_id=request.user.id)

        else:
            # Manejar formulario no válido
            pass
    else:
        form = ReservaForm(initial={'cabaña': cabaña})

    return render(request, 'reserva.html', {'form': form, 'cabaña': cabaña})

@login_required
def reservas_por_cliente(request, cliente_id):
    cliente = get_object_or_404(User, pk=cliente_id)
    reservas = Reserva.objects.filter(cliente=cliente)

    return render(request, 'verReservas.html', {'reservas': reservas, 'cliente': cliente})
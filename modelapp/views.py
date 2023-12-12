from django.shortcuts import get_object_or_404, redirect, render
from modelapp.models import Cabaña
from .models import Reserva, User 
from .forms import ReservaForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm



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
@login_required
def pagar(request, reservas_id):
    reserva = Reserva.objects.get(reserva_id=reservas_id)
    costo_total = calcular_costo_reserva(reserva)

    paypal_dict = {
        "business": "sb-kczmg28490318@business.example.com",
        "amount": costo_total,
        "item_name": "reserva numero: "+str(reserva.reserva_id),
        "invoice": reservas_id,
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri('/gracias'),
        "cancel_return": request.build_absolute_uri('/')
        }

        # Create the instance.
    formPaypal = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        'reserva': reserva,
        'costo_total': costo_total,
        'formPaypal':formPaypal

    }

    return render(request, "pagar.html", context)

def calcular_costo_reserva(reserva):
    duracion = (reserva.fecha_fin - reserva.fecha_inicio).days

    if duracion == 0:
        duracion = 1

    costo = duracion * reserva.cabaña.precio
    return costo

def gracias(request):

    return render(request,'gracias.html')
from django.shortcuts import get_object_or_404, redirect, render
from modelapp.models import Cabaña
from .forms import UserRegisterForm


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
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request,'register.html',context)
from django.shortcuts import get_object_or_404, render
from modelapp.models import Cabaña


def index(request):
    cabañas = Cabaña.objects.all();
    dict = { "datos": cabañas}
    
    return render(request,'index.html',dict)

def DetalleCabañas(request, cabaña_id):
    cabaña = get_object_or_404(Cabaña, cabaña_id=cabaña_id)
    return render(request, 'cabañas.html', {'cabaña': cabaña})
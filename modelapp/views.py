from django.shortcuts import render
from modelapp.models import Cabaña
def inicio(request):

    return render(request,'index.html')


def cabañas(request):
    cabañas = Cabaña.objects.all();
    dict = { "datos": cabañas}
    
    return render(request,'cabañas.html',dict)
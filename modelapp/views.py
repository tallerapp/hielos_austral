from django.shortcuts import render
from modelapp.models import Cabaña


def inicio(request):
    cabañas = Cabaña.objects.all();
    dict = { "datos": cabañas}
    
    return render(request,'index.html',dict)
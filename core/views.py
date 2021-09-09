from django.shortcuts import render
from .models import Muffin

# Create your views here.
def index(request):
    muffincitos = Muffin.objects.all()
    return render(request,'core/index.html',{'muffins':muffincitos})

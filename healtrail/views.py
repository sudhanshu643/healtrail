from django.shortcuts import render, HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    params = {}
    return render(request, 'index.html', {'products': products})
def service(request):
    products = Product.objects.all()
    print(products)
    params = {}    
    return render(request, 'service.html', {'products': products})
def yogas(request):
    return render(request, 'yogas.html')
def doctor(request):
    return render(request, 'doctor.html')    
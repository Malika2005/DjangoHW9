from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

def customers_info(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def customer_info(request, param):
    customer = Customer.objects.get(pk=param)
    return render(request, 'customer.html', {'customer': customer})

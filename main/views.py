from django.shortcuts import render
from . import models


def home(request):
    products = models.Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'base.html', context)
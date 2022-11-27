from django.shortcuts import render

from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True) #is_available=True --> brings only products that are in stock

    context = {
        'products': products,
    }
    return render(request, 'home.html', context)
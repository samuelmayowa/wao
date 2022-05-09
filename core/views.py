from django.shortcuts import render

from product.models import Product

def frontpage(request):
    newest_products = Product.objects.all()[0:12]
    return render(request, 'core/frontpage.html', {'newest_products': newest_products})







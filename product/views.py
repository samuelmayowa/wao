import random

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

from .forms import AddToCartForm, HireForm
from .models import Category, Product, Hire

from cart.cart import Cart

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products': products, 'query': query})

def contact(request):

    return render(request, 'product/contact.html')

def hire(request):

    return render(request, 'product/hire.html')

def aboutus(request):

    return render(request, 'product/aboutus.html')

def terms(request):

    return render(request, 'product/terms.html')

def safety(request):

    return render(request, 'product/safety.html')


def product(request, category_slug, product_slug):
    cart = Cart(request)

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'The product was added to the cart')

            return redirect('product', category_slug=category_slug, product_slug=product_slug)
    else:
        form = AddToCartForm()

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    return render(request, 'product/product.html', {'form': form, 'product': product, 'similar_products': similar_products})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'product/category.html', {'category': category})


def apply(request):
    if request.method == 'POST':
        form = HireForm(request.POST, request.FILES)


        if form.is_valid():
            messages.success(request, 'Your application has been submitted successfully')
            hire = form.save(commit=False)
            hire.slug = slugify(hire.name)
            hire.save()

            return redirect('hire')
    else:
        form = HireForm()

    return render(request, 'product/apply.html', {'form': form})




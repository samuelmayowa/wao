from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from vendor.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VendorForm
from .models import Files
from product.models import FileFieldForm
from .models import Vendor
from product.models import Product

from .forms import ProductForm, ProductImage, UserCreationForm
#from vendor.forms import RegistrationForm
from product.models import ProductImage, Product


def become_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name=user.email, created_by=user)

            #vendor = Vendor.objects.create(firstname=user.first_name, created_by=user)
            messages.success(request, "Welcome: Thanks for joining wao.ng. Click Post ads or Add Product to get started.")
            return redirect('vendor_admin')
        #messages.error(request, "Unsuccessful registration. Invalid information.")
        form = VendorForm()


    return render(request, 'vendor/become_vendor.html', {'VendorForm': VendorForm})


@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()

    return render(request, 'vendor/vendor_admin.html',{'vendor': vendor, 'products': products})



@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        file_list = []

        #for file in Files:
         #   new_file = Files(
          #      file = file
           # )
            #new_file.save()
            #file_list.append(new_file.image.url)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            messages.success(request, 'Thanks for using wao.ng, ads posted successfully')

            return redirect('add_images')
    else:
        form = ProductForm
        messages.success(request, "jpg, png, pdf ONLY")

    return render(request, 'vendor/add_product.html', {'form': form})


#START OF EDIT PRODUCT
@login_required
def edit_product(request, pk):
    vendor = request.user.vendor
    product = vendor.products.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        #START OF EXTENSION OF PODUCT FORM
        image_form = ProductImage(request.POST, request.FILES)

        #if image_form.is_valid():
         #   productimage = image_form.save(commit=False)
          #  productimage.product = product
           # productimage.save()
            ##END
            #return redirect('vendor_admin')


        if form.is_valid():
            form.save()

            return redirect('vendor_admin')
    else:
        form = ProductForm(instance=product)
        image_form = ProductImage()

    return render(request, 'vendor/edit_product.html', {'form': form, 'image_form': image_form, 'product': product})






#@login_required
#def add_product(request):
 #   if request.method == 'POST':
  #      form = ProductForm(request.POST, request.FILES)
   #     files = request.FILES.getlist('images')
    #    file_list = []
#
 ##          new_file = Files(
   #             file = file
    #        )
     #       new_file.save()
      #      file_list.append(new_file.file.url)

       # if form.is_valid():
        #    product = form.save(commit=False)
         #   product.vendor = request.user.vendor
          #  product.slug = slugify(product.title)
           # product.save()

            #return redirect('vendor_admin')
    #else:
     #   form = ProductForm()

    #return render(request, 'vendor/add_product.html', {'form': form})


#working addproduct view
#@login_require
#def add_product(request):
 #   if request.method == 'POST':
  #      form = ProductForm(request.POST, request.FILES)

   #     if form.is_valid():
    ##       product.vendor = request.user.vendor
      #      product.slug = slugify(product.title)
       #     product.save()

        #    return redirect('vendor_admin')
    #else:
     #   form = ProductForm()

    #return render(request, 'vendor/add_product.html', {'form': form})



@login_required
def edit_vendor(request):
    vendor = request.user.vendor

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        if name:
            vendor.created_by.email = email
            vendor.created_by.save()

            vendor.name = name
            vendor.save()

            return redirect('vendor_admin')

    return render(request, 'vendor/edit_vendor.html', {'vendor': vendor})


#Add Images
def addimages(TemplateView):
    template = "add_images.html"


    return redirect('vendor_admin')


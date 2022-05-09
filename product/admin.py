from django.contrib import admin

from .models import Category, Product, State, ProductImage, Hire

admin.site.register(Category)
#admin.site.register(Product)
admin.site.register(State)
admin.site.register(ProductImage)
admin.site.register(Hire)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'description', 'price', 'image', 'location_state', 'address','condition', 'status', 'phone_number']


admin.site.register(Product, ProductAdmin)
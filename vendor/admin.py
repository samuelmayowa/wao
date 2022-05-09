from django.contrib import admin

from .models import Vendor
from . models import Files
admin.site.register(Vendor)
admin.site.register(Files)

class VendorAdmin(admin.ModelAdmin):
    list_display = ['username', 'username', 'email', 'password1', 'password2']

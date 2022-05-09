from django.forms import TextInput, EmailInput
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from product.models import Product, File, ProductImage
from vendor.models import Vendor


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = {'category',
				  'title',
				  'business_name',
				  'condition',
				  'phone_number',
				  'price','description',
				  'location_state',
				  'address',
				  'image',
				  }

class VendorForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	first_name = forms.CharField(max_length=30, required=False, label='Fornavn', help_text='Optional.', widget=forms.TextInput(attrs={'placeholder': 'Name'}))


	class Meta:
		model = User

		fields = ("username", "first_name", "email", "password1", "password2")


	def save(self, commit=True):
		user = super(VendorForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']
		user.first_name = self.cleaned_data['first_name']
		if commit:
			user.save()
		return user


#class RegistrationForm(UserCreationForm):
 #   username = None

  #  first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
   # last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    #email = forms.EmailField(required=True, max_length=254, help_text='Enter a valid email address')

    #class Meta:
     #   model = Vendor
      #  fields = {'email', 'firstname', 'lastname', 'password1', 'password2'}

       # def save(self, commit=True):
        #    vendor = super(RegistrationForm, self).save(commit=False)
         ### vendor.last_name = self.cleaned_data["first_name"]
            #if commit:
             #   vendor.save()
            #return Vendor

class ProductImage(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['images']
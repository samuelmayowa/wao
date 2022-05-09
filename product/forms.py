from django import forms
from .models import Hire
from django.forms import ModelForm

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()

class HireForm(ModelForm):
    class Meta:
        model = Hire
        fields = {'state', 'name', 'email', 'availability', 'phone_number', 'qualification', 'upload_cv'}
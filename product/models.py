from django.core.validators import FileExtensionValidator
from django import forms
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

from vendor.models import Vendor




class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)


    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title

class State(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)


    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def __str__(self):
        return self.file_field

#STate

#END
class Product(models.Model):
    STATUS_AVAILABLE = 'Available'
    STATUS_PREORDER = 'Pre Order Only'
    STATUS_SOLD = 'Sold'


    STATUS_CHOICES = [
        (STATUS_AVAILABLE, 'Available'),
        (STATUS_PREORDER, 'Pre Order Only'),
        (STATUS_SOLD, 'Sold'),
    ]
    CONDITION_NEW = 'New'
    CONDITION_FOREIGNUSED = 'Foreign Used'
    CONDITION_USED = 'Sold'

    CONDITION_CHOICES = [
        (CONDITION_NEW, 'New'),
        (CONDITION_FOREIGNUSED, 'Foreign Used'),
        (CONDITION_USED, 'Used'),
    ]

    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    business_name = models.CharField(max_length=255, blank=True, null=True)
    type = models.TextField(max_length=255, blank=True, null=True)
    condition = models.CharField(
        max_length=20, choices=CONDITION_CHOICES, default=CONDITION_NEW)
    phone_number = models.CharField(max_length=255)
    location_state = models.ForeignKey(State, related_name='products', on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        verbose_name=("Price"),
        error_messages={
            "name": {
                "max_length": ("Please Enter a fair price"),
            },
        },
        max_digits=10,
        decimal_places=2, default=0
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_AVAILABLE)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='uploads/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['xml', 'jpg', 'png',])])
    thumbnail = models.FileField(upload_to='uploads/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['xml', 'jpg', 'png',])])

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default='None', on_delete=models.CASCADE)
    images = models.FileField(upload_to='uploads/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['xml', 'jpg', 'png',])])

    def __str__(self):
        return self.product.title

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.images:
                self.thumbnail = self.make_thumbnail(self.images)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, images, size=(300, 200)):
        img = Image.open(images)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=images.name)

        return thumbnail


#START OF HIRE FORM MODEL
class Hire(models.Model):
    STATUS_AVAILABLE = 'Immediately '
    STATUS_PREORDER = 'One Month Notice'
    STATUS_SOLD = 'Yet to decide'


    AVAILABILITY_CHOICES = [
        (STATUS_AVAILABLE, 'Immediately'),
        (STATUS_PREORDER, 'One Month Notice'),
        (STATUS_SOLD, 'Yet to decide'),
    ]
    QUALIFICATION_ONE = 'OND '
    QUALIFICATION_TWO = 'HND'
    QUALIFICATION_THREE= 'Bachelor'
    QUALIFICATION_FOUR = 'Others'

    QUALIFICATION_CHOICES = [
        (QUALIFICATION_ONE, 'OND'),
        (QUALIFICATION_TWO, 'HND'),
        (QUALIFICATION_THREE, 'Bachelor'),
        (QUALIFICATION_FOUR, 'Others'),
    ]

    state = models.ForeignKey(State, related_name='hires', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    availability = models.CharField(
        max_length=20, choices=AVAILABILITY_CHOICES, default=STATUS_AVAILABLE)
    phone_number = models.CharField(max_length=255)
    qualification = models.CharField(
        max_length=20, choices=QUALIFICATION_CHOICES, default=QUALIFICATION_ONE)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)
    upload_cv = models.FileField(upload_to='uploads/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['doc', 'pdf', 'jpeg', 'png'])])
    thumbnail = models.FileField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

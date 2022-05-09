from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
#from formatChecker import ContentTypeRestrictedFileField

class Files(models.Model):
    file = models.FileField(upload_to='file', validators=[FileExtensionValidator(allowed_extensions=['xml', 'jpg', 'png',])])

class Vendor(models.Model):
    MEMBERSHIP_STANDARD = 'S'
    MEMBERSHIP_PREMIUM = 'P'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_STANDARD, 'Standard'),
        (MEMBERSHIP_PREMIUM, 'Premium'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    name = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(max_length=200, null=True, unique=True)
    phone_number = models.CharField(max_length=200, null=True)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_STANDARD)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
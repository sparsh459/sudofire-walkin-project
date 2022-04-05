from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class UserModel(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    number = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self) -> str:
        return self.fname

class CustomerModel(models.Model):
    profileN = models.OneToOneField(UserModel, null=True, on_delete=models.CASCADE)

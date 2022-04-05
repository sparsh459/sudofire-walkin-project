from django.contrib import admin
from sudoapi.models import UserModel, CustomerModel

# Register your models here.
@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'fname', 'lname', 'email', 'number']

@admin.register(CustomerModel)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'profileN']

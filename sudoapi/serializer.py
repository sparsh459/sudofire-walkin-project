from sudoapi.models import UserModel, CustomerModel
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'fname', 'lname', 'email', 'number']
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ['id', 'profileN']

from rest_framework import serializers
from .models import Customer, Contracts, BankDetail
from rest_framework.exceptions import PermissionDenied


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:

        model = Contracts
        fields = '__all__'
        ordering = ['-id']

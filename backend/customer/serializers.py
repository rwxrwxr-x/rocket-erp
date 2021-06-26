from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import BankDetail
from .models import Contracts
from .models import Customer


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields = self.context['request'].query_params.get('fields')
        if fields:
            fields = fields.split(',')
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = ['name', 'bic', 'account', 'c_account']


class CustomerSerializer(serializers.ModelSerializer):
    customer_bank = BankDetailSerializer()

    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'jp', 'inn', 'customer_bank')


class ContractSerializer(DynamicFieldsModelSerializer):
    def create(self, validated_data, *args, **kwargs):
        customer_id = self.context.get('customer_id')
        customer = get_object_or_404(Customer, pk=customer_id)
        contract = Contracts.objects.create(customer=customer,
                                            **validated_data)
        return contract

    class Meta:
        model = Contracts
        fields = ('id', 'name', 'customer')
        read_only_fields = ('customer',)

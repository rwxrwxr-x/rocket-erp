from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import BankDetail
from .models import Contracts
from .models import Customer


class BankDetailSerializer(serializers.ModelSerializer):
    """Basic bank detail serializer."""
    class Meta:
        model = BankDetail
        fields = ['name', 'bic', 'account', 'c_account']


class CustomerSerializer(serializers.ModelSerializer):
    """Basic customer serializer."""
    customer_bank = BankDetailSerializer()

    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'jp', 'inn', 'customer_bank')


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = ('id', 'name', 'customer')


class ContractSubSerializer(ContractSerializer):
    """Contract serializer with override create method."""
    def create(self, validated_data, *args, **kwargs):
        customer_id = self.context.get('customer_id', None)
        if customer_id:
            customer = get_object_or_404(Customer, pk=customer_id)
            contract = Contracts.objects.create(customer=customer,
                                                **validated_data)
            return contract
        else:
            return super().create(validated_data)

    class Meta(ContractSerializer.Meta):
        fields = ContractSerializer.Meta.fields


class CurrentlyCustomersSerializer(CustomerSerializer):
    """Returns Customers with active projects."""

    active_contracts = ContractSerializer(source="get_contracts", many=True)

    class Meta(CustomerSerializer.Meta):
        fields = ('id', 'name', 'active_contracts')

from rest_framework.serializers import ModelSerializer

from rocket_erp.apps.accounts.models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

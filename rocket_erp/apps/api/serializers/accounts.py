from rest_framework.serializers import ModelSerializer

from rocket_erp.apps.accounts.models import Account


class AccountSerializer(ModelSerializer):
    """Serializer for account app, with all fields."""

    class Meta:
        model = Account
        fields = "__all__"

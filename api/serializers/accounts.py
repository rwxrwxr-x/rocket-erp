from rest_framework.serializers import ModelSerializer

from accounts.models import Account


class AccountSerializer(ModelSerializer):
    """Serializer for account app, with all fields."""

    class Meta:
        model = Account
        fields = "__all__"

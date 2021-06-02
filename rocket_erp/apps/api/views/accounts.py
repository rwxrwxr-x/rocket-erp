from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from rocket_erp.apps.accounts.models import Account


class LargeResultsSetPagination(PageNumberPagination):
    """Account pagination."""

    page_size = 5


class AccountViewSet(ModelViewSet):
    """Api account view."""

    serializer_class = None
    queryset = Account.objects.all()
    pagination_class = LargeResultsSetPagination

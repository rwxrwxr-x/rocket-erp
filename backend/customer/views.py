from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from ..api.utils import SubViewCreateModelMixin
from ..api.utils import SubViewListModelMixin
from ..api.utils import SubViewSet
from .models import BankDetail
from .models import Contracts
from .models import Customer
from .serializers import BankDetailSerializer
from .serializers import ContractSubSerializer
from .serializers import CurrentlyCustomersSerializer
from .serializers import CustomerSerializer


@swagger_auto_schema(methods=['get'],
                     responses={status.HTTP_200_OK:
                                CurrentlyCustomersSerializer(many=True)})
@api_view(['GET'])
def get_active_customers(request):
    """Get a list of customers whose projects are curated by the user."""
    query = Customer.objects.filter(
        customer_contracts__project__project_curator__account_id
        =request.user.id,
        customer_contracts__project__is_completed=False,
        customer_contracts__project__is_cancelled=False)
    serializer = CurrentlyCustomersSerializer(query, many=True)
    return Response(serializer.data)


class ContractViewSet(SubViewCreateModelMixin, SubViewListModelMixin,
                      SubViewSet):
    """ContractViewSet, methods = list, create, update, patch."""
    serializer_class = ContractSubSerializer
    queryset = Contracts.objects.order_by('-id')
    primary_id = 'customer_id'


class CustomerViewSet(CreateModelMixin, SubViewListModelMixin, SubViewSet):
    """CustomerViewSet, methods = list, create, update, patch."""
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class BankDetailView(SubViewCreateModelMixin, SubViewSet):
    """BankDetailViewSet, methods = create, update, patch."""
    serializer_class = BankDetailSerializer
    queryset = BankDetail.objects.order_by('-id')
    primary_id = 'customer_id'

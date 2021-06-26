from rest_framework.mixins import CreateModelMixin

from ..api.utils import SubViewCreateModelMixin
from ..api.utils import SubViewListModelMixin
from ..api.utils import SubViewSet
from .models import BankDetail
from .models import Contracts
from .models import Customer
from .serializers import BankDetailSerializer
from .serializers import ContractSerializer
from .serializers import CustomerSerializer


class ContractViewSet(SubViewCreateModelMixin, SubViewListModelMixin, SubViewSet):
    serializer_class = ContractSerializer
    queryset = Contracts.objects.order_by('-id')
    primary_id = 'customer_id'


class CustomerViewSet(CreateModelMixin, SubViewListModelMixin, SubViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class BankDetailView(SubViewCreateModelMixin, SubViewSet):
    serializer_class = BankDetailSerializer
    queryset = BankDetail.objects.order_by('-id')
    primary_id = 'customer_id'

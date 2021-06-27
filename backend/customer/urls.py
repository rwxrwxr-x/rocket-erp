from django.urls import include
from django.urls import path
from django.urls import re_path
from rest_framework import routers

from .views import BankDetailView
from .views import ContractViewSet
from .views import CustomerViewSet
from .views import get_active_customers

router = routers.DefaultRouter()
router.register(r'', CustomerViewSet, 'customer')
router.register(r'^(?P<customer_id>[-\w]+)/bank', BankDetailView, 'bankdetail')
router.register(r'^(?P<customer_id>[-\w]+)/contract', ContractViewSet, 'contract')
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'active', get_active_customers)
]

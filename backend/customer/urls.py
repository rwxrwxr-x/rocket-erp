from django.urls import include
from django.urls import path
from rest_framework import routers

from .views import BankDetailView
from .views import ContractViewSet
from .views import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'', CustomerViewSet, 'customer')
router.register(r'^(?P<customer_id>[-\w]+)/bank', BankDetailView, 'bankdetail')
router.register(r'^(?P<customer_id>[-\w]+)/contract', ContractViewSet, 'contract')
urlpatterns = [
    path('', include(router.urls)),
]

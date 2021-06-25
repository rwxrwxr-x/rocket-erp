from django.urls import path, re_path, include
from .views import CustomerViewSet, ContractViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', CustomerViewSet, 'customer')
router.register(r'^(?P<customer_id>[-\w]+)/contract', ContractViewSet, 'contract')
urlpatterns = [
    path('', include(router.urls)),
]
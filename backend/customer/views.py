from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, ListModelMixin, \
    RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Customer, Contracts
from .serializers import CustomerSerializer, ContractSerializer


class ContractViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin,
                      UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = ContractSerializer
    queryset: Contracts.objects = Contracts.objects.order_by('-id')

    def retrieve(self, request, customer_id=None, pk=None, *args, **kwargs):
        queryset = self.queryset.filter(customer_id=customer_id)
        contract = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(contract)
        return Response(serializer.data)

    def list(self, request, customer_id=None, *args, **kwargs):
        queryset = self.queryset.filter(customer_id=customer_id)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CustomerViewSet(CreateModelMixin, RetrieveModelMixin,
                      UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def retrieve(self, request, pk=None, *args, **kwargs):
        customer = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(customer)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        serializer_instance = get_object_or_404(self.queryset, pk=pk)
        partial = kwargs.get('partial', None)
        serializer = self.serializer_class(
            serializer_instance,
            context={'request': request},
            data=request.data,
            partial=partial
        )
        serializer.is_valid()
        serializer.save()
        return Response(request.data)

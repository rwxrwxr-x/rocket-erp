from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response


class SubViewCreateModelMixin(CreateModelMixin):
    """
    CreateModelMixin for SubViewSet
    """
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request,
                     self.primary_id: kwargs.get(self.primary_id)}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SubViewListModelMixin(ListModelMixin):
    """
    ListModelMixin for SubViewSet.
    """
    def list(self, request, *args, **kwargs):
        queryset = self.get_primary_queryset(kwargs) or self.queryset
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SubViewSet(RetrieveModelMixin,
                 UpdateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet that work with an subview argument specified (primary_id).
    """

    primary_id = ''

    def get_primary(self, kwargs):
        return kwargs.get(self.primary_id, None)

    def get_primary_queryset(self, kwargs):
        primary = self.get_primary(kwargs)
        if primary:
            queryset = self.queryset.filter(**{self.primary_id: primary})
            return queryset
        else:
            return None

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = self.get_primary_queryset(kwargs) or self.queryset
        result = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(result)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        queryset = self.get_primary_queryset(kwargs) or self.queryset
        serializer_instance = get_object_or_404(queryset, pk=pk)
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

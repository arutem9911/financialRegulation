from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from web.models import FinancialOrganization, Executive
from api.serializes import FinOrgSerializer, ExecutiveSerializer
from django.contrib.auth import get_user_model


# Create your views here.
class FinOrgViewSet(ModelViewSet):
    queryset = FinancialOrganization.objects.all()
    serializer_class = FinOrgSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class ExecutiveViewSet(ModelViewSet):
    queryset = Executive.objects.all()
    serializer_class = ExecutiveSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

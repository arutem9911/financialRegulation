from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from web.models import FinancialOrganization, Manager
from api.serializes import FinOrgSerializer, ManagerSerializer
from django.contrib.auth import get_user_model


# Create your views here.
class FinOrgViewSet(ModelViewSet):
    queryset = FinancialOrganization.objects.all()
    serializer_class = FinOrgSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class ManagerViewSet(ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

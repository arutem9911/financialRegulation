from rest_framework import serializers
from web.models import FinancialOrganization, Manager


class FinOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialOrganization
        fields = ['id', 'name', 'BIN', 'address', 'phone', 'fax', 'email', 'web_site']
        read_only = ['id']


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'full_name', 'IIN', 'job_title', 'phone', 'email', 'fin_organization']
        read_only_fields = ['id']


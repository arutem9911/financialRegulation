from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django import shortcuts
# from web.forms import VacancyForm, SummaryForm, SearchForm, ResponseForm
from web.models import FinancialOrganization, Manager
from urllib.parse import urlencode
from django.db.models import Q


class FinOrgs(ListView):
    template_name = 'finOrgsList.html'
    model = FinancialOrganization
    context_object_name = 'finOrgs'


class FinOrgDetail(DetailView):
    template_name = 'FinOrgDetail.html'
    model = FinancialOrganization
    context_object_name = 'FinOrg'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        fn_org_managers = self.object.managers.all()
        managers = []
        for item_manager in fn_org_managers:
            managers.append(item_manager)
        return super().get_context_data(
            managers=managers,
            **kwargs
        )

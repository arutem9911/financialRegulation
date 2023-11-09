from django.contrib import admin

from web.models import *


class FinancialOrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'BIN', 'address', 'phone', 'fax', 'email', 'web_site']
    list_filter = ['name', 'BIN']
    search_fields = ['name', 'BIN', 'address', 'web_site']
    fields = ['name', 'BIN', 'address', 'phone', 'fax', 'email', 'web_site']


class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'IIN', 'job_title', 'phone', 'email', 'fin_organization']
    list_filter = ['full_name', 'job_title', 'fin_organization']
    search_fields = ['full_name', 'IIN', 'job_title', 'fin_organization']
    fields = ['full_name', 'IIN', 'job_title', 'phone', 'email', 'fin_organization']


class WorkPeriodAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_date', 'end_date', 'executive']
    fields = ['start_date', 'end_date', 'executive']


admin.site.register(FinancialOrganization, FinancialOrganizationAdmin)
admin.site.register(Executive, ExecutiveAdmin)
admin.site.register(WorkPeriod, WorkPeriodAdmin)


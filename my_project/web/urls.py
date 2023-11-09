from django.urls import path
from web import views


urlpatterns = [
   path('', views.FinOrgs.as_view(), name='fin_orgs_list'),
   path('detailFinOrg/<int:id>', views.FinOrgDetail.as_view(), name='detail-fin-org'),

]

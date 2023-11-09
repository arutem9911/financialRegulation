from django.urls import path, include
from rest_framework import routers
from .views import FinOrgViewSet, ManagerViewSet


router = routers.DefaultRouter()
router.register('finOrg', FinOrgViewSet)
router.register('manager', ManagerViewSet)


urlpatterns = [
    path('', include(router.urls))
]

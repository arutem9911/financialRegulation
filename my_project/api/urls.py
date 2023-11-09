from django.urls import path, include
from rest_framework import routers
from .views import FinOrgViewSet, ExecutiveViewSet


router = routers.DefaultRouter()
router.register('finOrg', FinOrgViewSet)
router.register('executive', ExecutiveViewSet)


urlpatterns = [
    path('', include(router.urls))
]

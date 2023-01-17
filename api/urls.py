
from django.contrib import admin
from django.urls import path, include
from api.views import OpportunityViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'opportunities', OpportunityViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

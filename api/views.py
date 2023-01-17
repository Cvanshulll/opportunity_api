from django.shortcuts import render
from rest_framework import viewsets
from api.models import Opportunity
from api.serializers import OpportunitySerializer
# Create your views here.
class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
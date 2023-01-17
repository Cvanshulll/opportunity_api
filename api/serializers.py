from rest_framework import serializers
from api.models import Opportunity
# Create your serializers here.
class OpportunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        company_id  = serializers.ReadOnlyField()
        model = Opportunity
        fields = "__all__"
        # fields = ('opportunity_id', 'name', 'location', 'role', 'description', 'start_date', 'date', 'added_date', 'active', 'image', 'created_at', 'updated_at')
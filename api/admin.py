from django.contrib import admin
from api.models import Opportunity
# Register your models here.


class OpportunityAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'role')
    # list_display_links = ('name')
    search_fields = ('name', 'role')
    list_filter = ('name', 'role')
    list_per_page = 25

admin.site.register(Opportunity, OpportunityAdmin)
from django.contrib import admin

from providers.models import *
from providers.apps import *

# ProviderModel = str(ProvidersConfig.name+"."+ ProvidersConfig.ProviderModel)

class Provider_Admin(admin.ModelAdmin):
    # list_display = ('phone_number', 'language', 'currency')
    # list_filter = ['phone_number']
    # search_fields = ['phone_number']
    pass

admin.site.register(ProviderModel) 
# ===========================================================
admin.site.register(ServiceModel) 

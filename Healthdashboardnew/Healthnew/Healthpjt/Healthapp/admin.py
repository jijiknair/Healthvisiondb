from django.contrib import admin
from . models import diseasestreemap
from . models import Disease
from . models import Servicenew
from . models import Subservicenew
from . models import Subservice
# Register your models here.
admin.site.register(diseasestreemap)
admin.site.register(Disease)
admin.site.register(Servicenew)
admin.site.register(Subservicenew)
admin.site.register(Subservice)
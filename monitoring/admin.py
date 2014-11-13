from django.contrib import admin
from monitoring.models import Account, Location, SensorGroup, Reading

# Register your models here.
admin.site.register(Account)
admin.site.register(Location)
admin.site.register(SensorGroup)
admin.site.register(Reading)


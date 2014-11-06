from django.contrib import admin
from monitoring.models import Account, Contact, Location, SensorGroup, Reading

# Register your models here.
admin.site.register(Account)
admin.site.register(Contact)
admin.site.register(Location)
admin.site.register(SensorGroup)
admin.site.register(Reading)


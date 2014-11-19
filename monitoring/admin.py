from django.contrib import admin
from monitoring.models import Location, SensorGroup, Reading

# Register your models here.
admin.site.register(Location)
admin.site.register(SensorGroup)
admin.site.register(Reading)


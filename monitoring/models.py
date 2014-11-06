from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
	country = models.CharField(max_length=100)
	state = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=100)
	street_address = models.CharField(max_length=175)
	zip_code = models.CharField(max_length=10, null=True)
	description = models.CharField(max_length=200, null=True)
	def __str__(self):
		if self.description is None:
			return self.country + ' ' + self.state + ' ' + self.street_address
		return self.description

class Account(models.Model):
	name = models.CharField(max_length=75)
	start_date = models.DateTimeField('datetime started')
	end_date = models.DateTimeField('datetime terminated', null=True)
	def __str__(self):
		return self.name

class Contact(models.Model):
    user = models.OneToOneField(User)
    account = models.ForeignKey(Account)
    location = models.ForeignKey(Location, null=True)
    phone = models.CharField(max_length=10, null=True)
    def __str__(self):
		return self.first_name + ' ' + self.last_name

class SensorGroup(models.Model):
	location = models.ForeignKey(Location)
	account = models.ForeignKey(Account)
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=250, null=True)
	is_active = models.BooleanField(default=True)
	def __str__(self):
		return self.name

class Reading(models.Model):
	sensor_group = models.ForeignKey(SensorGroup)
	type = models.CharField(max_length=20)
	data = models.CharField(max_length=200)
	date = models.DateTimeField('datetime received')
	def __str__(self):
		return self.type + '  '+ self.data


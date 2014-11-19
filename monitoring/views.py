from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from models import SensorGroup, Location, Reading
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

def register_user(request):
    if request.method == 'POST':
        form = 4
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/monitoring/register_success')
    args = {}
    args.update(csrf(request))
    return render_to_response('monitoring/register.html', args)

def register_success(request):
    return render_to_response('monitoring/register_success.html')

def locations_view(request):
    sensor_location_list = []
    sensors = SensorGroup.objects.filter(user__id = 1)
    for sensor in sensors:
    	location = Location.objects.filter(sensorgroup = sensor.id)
    	location_string = location[0].country + ' ' + location[0].state + ' ' + location[0].city + location[0].street_address
    	sensor_location_tuple = (sensor.id, sensor.name, location_string)
    	sensor_location_list.append(sensor_location_tuple)
    template = loader.get_template('monitoring/locations.html')
    context = RequestContext(request, {'sensor_location_list' : sensor_location_list})
    return HttpResponse(template.render(context))

def readings_view(request, sensor_id):
	sensor_readings = []
	latest_ph = Reading.objects.filter(sensor_group_id = sensor_id, type = 'pH').latest('date')
	latest_ec = Reading.objects.filter(sensor_group_id = sensor_id, type = 'EC').latest('date')
	sensor_readings.append(latest_ph)
	sensor_readings.append(latest_ec)

	sensor = SensorGroup.objects.filter(id = sensor_id)[0]
	sensor_name = sensor.name
	sensor_location = sensor.location.description

	template = loader.get_template('monitoring/readings.html')
	context = RequestContext(request, {'sensor_readings':sensor_readings, 'sensor_name':sensor_name, 'sensor_location':sensor_location})
	return HttpResponse(template.render(context))

@csrf_exempt
def get_readings(request):
    if request.method == 'POST':
        #arduino_reading = request.POST['type'] + ' ' + request.POST['date'] + ' ' + request.POST['reading']
        s = SensorGroup.objects.all()[0]
        r = Reading(sensor_group_id=s.id, type=request.POST['type'], data=request.POST['reading'], date=request.POST['date'])
        r.save()
        return HttpResponse('Success')
    else:
        return HttpResponse('No readings')

